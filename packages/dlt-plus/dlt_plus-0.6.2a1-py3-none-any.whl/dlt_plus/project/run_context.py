import os
import re
import sys
import argparse
from types import ModuleType
import tomlkit
from dataclasses import dataclass
from contextlib import contextmanager
from typing import Any, Dict, Iterator, List, Optional

from dlt.common import known_env
from dlt.common.configuration.specs.pluggable_run_context import SupportsRunContext
from dlt.common.configuration.container import Container
from dlt.common.configuration.exceptions import ContainerInjectableContextMangled
from dlt.common.configuration.specs.pluggable_run_context import PluggableRunContext
from dlt.common.configuration.providers import (
    EnvironProvider,
    ConfigTomlProvider,
)
from dlt.common.configuration.providers.provider import ConfigProvider
from dlt.common.runtime.run_context import RunContext, DOT_DLT, global_dir
from dlt.reflection.script_inspector import import_pipeline_script

from dlt_plus.common.constants import DEFAULT_PROJECT_CONFIG_FILE
from dlt_plus.common.configuration.providers import ProfileSecretsTomlProvider

from .config.config import Project
from .config.config_loader import ConfigLoader
from .exceptions import ProjectRunContextNotAvailable


class ProjectRunContext(SupportsRunContext):
    def __init__(self, run_dir: Optional[str]):
        self._project_dir = run_dir
        self._config: Project = None
        self._default_context = RunContext(run_dir=run_dir)
        self._adhoc_sys_path: str = None

    @property
    def name(self) -> str:
        """Returns run dlt package name: as defined in the project yaml or the parent folder name
        if not defined"""
        return self._config.name or os.path.basename(self.run_dir)

    @property
    def global_dir(self) -> str:
        """Directory in which global settings are stored ie ~/.dlt/"""
        return self._default_context.global_dir

    @property
    def run_dir(self) -> str:
        """A folder containing dlt project file"""
        return os.environ.get(known_env.DLT_PROJECT_DIR, self._project_dir)

    @property
    def settings_dir(self) -> str:
        """Defines where the current settings (secrets and configs) are located"""
        return os.path.join(self.run_dir, DOT_DLT)

    @property
    def data_dir(self) -> str:
        """Isolates data for pipelines by packages and profiles ie. ~.dlt/dlt-pond-demo/dev/"""
        home_dir = self._default_context.data_dir
        return os.path.join(home_dir, self.name, self.profile)

    def initial_providers(self) -> List[ConfigProvider]:
        providers = [
            EnvironProvider(),
            # load secrets from profiled tomls ie. dev.secrets.toml. use secrets.toml as global
            ProfileSecretsTomlProvider(
                self.settings_dir, self.config.current_profile, self.global_dir
            ),
            # use regular config.toml without profiles, allow for global settings
            ConfigTomlProvider(self.settings_dir, self.global_dir),
            # add project as config provider
            self._config.provider(provider_name=self.name),
        ]
        return providers

    @property
    def module(self) -> Optional[ModuleType]:
        try:
            return RunContext.import_run_dir_module(self.run_dir)
        except ImportError:
            return None

    @property
    def runtime_kwargs(self) -> Dict[str, Any]:
        return {"profile": self.profile}

    @property
    def profile(self) -> str:
        return self._config.current_profile

    @property
    def config(self) -> Project:
        return self._config

    @config.setter
    def config(self, project: Project) -> None:
        self._config = project

    @property
    def tmp_dir(self) -> str:
        return self._config.tmp_dir

    def get_data_entity(self, entity: str) -> str:
        """Gets path in data_dir where `entity` (ie. `pipelines`, `repos`) are stored"""
        return os.path.join(self.data_dir, entity)

    def get_run_entity(self, entity: str) -> str:
        """Gets path in run_dir where `entity` (ie. `sources`, `destinations` etc.) are stored"""
        return os.path.join(self.run_dir, entity)

    def get_setting(self, setting_path: str) -> str:
        """Gets path in settings_dir where setting (ie. `secrets.toml`) are stored"""
        return os.path.join(self.settings_dir, setting_path)

    def unplug(self) -> None:
        # remove added sys path
        if self._adhoc_sys_path:
            if self._adhoc_sys_path in sys.path:
                sys.path.remove(self._adhoc_sys_path)
            self._adhoc_sys_path = None

    def plug(self) -> None:
        # create temp and data dirs
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.tmp_dir, exist_ok=True)

    def switch_profile(self, new_profile: str) -> "ProjectRunContext":
        """Switches current profile and returns new run context"""
        return switch_profile(new_profile)

    def switch_context(
        self, project_dir: Optional[str], profile: str = None
    ) -> "ProjectRunContext":
        """Switches the context to `project_dir` and `profile` is provided"""
        return switch_context(project_dir, profile=profile)

    @staticmethod
    def ensure_importable(run_dir: str) -> Optional[str]:
        """Adds current project to syspath if it is not a module already.

        Allow to create an ad hoc flat Python packages.
        Returns new syspath if added
        """
        try:
            # try to import as regular package
            RunContext.import_run_dir_module(run_dir)
            return None
        except ImportError:
            # add to syspath if necessary
            if run_dir in sys.path:
                return None
            sys.path.append(run_dir)
            return run_dir


@dataclass
class InstalledDltPackageInfo:
    package_name: str
    module_name: str
    docstring: str
    license_scopes: str = None


def read_profile_pin(context: ProjectRunContext) -> str:
    # load profile name from .profile-name
    profile_pin = context.get_setting("profile-name")
    if os.path.isfile(profile_pin):
        with open(profile_pin, "tr", encoding="utf-8") as pin:
            return pin.readline().strip()
    return None


def save_profile_pin(context: ProjectRunContext, profile: str) -> None:
    # load profile name from .profile-name
    profile_pin = context.get_setting("profile-name")
    with open(profile_pin, "wt", encoding="utf-8") as pin:
        pin.write(profile)


def create_project_context(project_dir: str, profile: str = None) -> ProjectRunContext:
    """Creates a project context in `project_dir` and switches to `profile`.

    - Uses dlt.yml if found in `project_dir`
    - Otherwise creates a project with an empty (default) config
    - Makes sure that Python code in `project_dir` is importable

    If dirname(project_dir) is a Python module: all OK (package structure)
    If not we assume flat structure and we add project_dir to syspath
    """
    project_dir = os.path.abspath(project_dir)
    add_import_path = ProjectRunContext.ensure_importable(project_dir) if project_dir else None

    try:
        manifest_path = os.path.join(project_dir, DEFAULT_PROJECT_CONFIG_FILE)
        if not os.path.isfile(manifest_path):
            raise ProjectRunContextNotAvailable(project_dir, RunContext(run_dir=None))

        config_loader = ConfigLoader.from_file(
            os.path.join(project_dir, DEFAULT_PROJECT_CONFIG_FILE)
        )

        # make preliminary context to access settings
        context = ProjectRunContext(project_dir)
        context._adhoc_sys_path = add_import_path
        profile = profile or read_profile_pin(context)

        # bind project to context
        context.config = config_loader.get_config(profile=profile)
        return context
    except Exception:
        # always remove import path on exception
        if add_import_path:
            sys.path.remove(add_import_path)
        raise


def switch_profile(profile: str) -> ProjectRunContext:
    """Changes active profile and reloads context"""

    ctx = Container()[PluggableRunContext].context
    if not isinstance(ctx, ProjectRunContext):
        raise ProjectRunContextNotAvailable(ctx.run_dir, ctx)
    return switch_context(None, profile=profile)


def switch_context(project_dir: Optional[str], profile: str = None) -> ProjectRunContext:
    container = Container()
    cookie = container[PluggableRunContext].push_context()
    add_import_path = ProjectRunContext.ensure_importable(project_dir) if project_dir else None
    try:
        # reload run context via plugins
        container[PluggableRunContext].reload(project_dir, dict(profile=profile))

        # return new run context
        ctx = container[PluggableRunContext].context
        if not isinstance(ctx, ProjectRunContext):
            raise ProjectRunContextNotAvailable(ctx.run_dir, ctx)
        ctx._adhoc_sys_path = add_import_path
        container[PluggableRunContext].drop_context(cookie)
        return ctx
    except Exception:
        if add_import_path:
            sys.path.remove(add_import_path)
        # restore context if switch fails
        container[PluggableRunContext].pop_context(cookie)
        raise


@contextmanager
def injected_run_context(new_context: SupportsRunContext = None) -> Iterator[None]:
    container = Container()
    cookie = container[PluggableRunContext].push_context()
    if new_context:
        container[PluggableRunContext].context = new_context
        container[PluggableRunContext].reload_providers()
    try:
        yield
    finally:
        # do not allow context to be changed
        if new_context:
            existing_context = container[PluggableRunContext].context
            if existing_context != new_context:
                raise ContainerInjectableContextMangled(
                    new_context.__class__, existing_context, new_context
                )
        container[PluggableRunContext].pop_context(cookie)


def import_context_from_dir(project_dir: str, profile: str = None) -> None:
    """(POC) Imports entities in a given context.
    Initial version to prove the concept of separate imports"""
    ctx = create_project_context(project_dir, profile=profile)

    with injected_run_context(ctx):
        # TODO: allow to import script from folder that are package (__init__.py) and without
        # TODO: we assume that __init__ import all sources
        import_pipeline_script(ctx.run_dir, "sources")


def import_context_from_dist(dist: str) -> None:
    """Import entities form a Python distribution `dist` which contains run context"""
    raise NotImplementedError()


# def find_module_run_dir(module_: str) -> str:
#     """Finds run context in `dist` that follows standard package layout"""
#     if dist is None:
#         # use pyproject


def find_pyproject_project_dir(dist_path: str) -> str:
    """Finds run context by inspecting pyproject.toml in distribution path `dist_path`

    1. pyproject that explicitly defines Python package via `dlt_package` entry point
    2. if not, we use package name to identify Python module path where we expect the project_dir

    In case of (2) project dir must contain dlt.yml or .dlt
    """
    dist_path = os.path.abspath(dist_path)

    # load pyproject or exit
    pyproject_path = os.path.join(dist_path, "pyproject.toml")
    if not os.path.isfile(pyproject_path):
        return None
    with open(pyproject_path, "r", encoding="utf-8") as f:
        pyproject_data = tomlkit.load(f)

    # check explicit pointer to dlt package
    package_ep = ((pyproject_data.get("project") or {}).get("entry-points") or {}).get(
        "dlt_package"
    )
    if package_ep:
        package_name = package_ep.get("dlt-project")
    else:
        package_name = (pyproject_data.get("project") or {}).get("name")

    if not package_name:
        return None
    # convert the package name to a valid module directory name
    package_dir_name = re.sub(r"\W|^(?=\d)", "_", package_name.lower())

    # support two layouts
    for src_dir in [package_dir_name, os.path.join("src", package_dir_name)]:
        project_dir = os.path.join(dist_path, src_dir)
        if os.path.isdir(project_dir):
            if package_ep or is_project_dir(project_dir):
                return project_dir
    return None


def find_project_dir() -> str:
    """Look for dlt project dir, starting in cwd(), with following rules:

    - look for `pyproject.toml` and check if it points to dlt project
    - if not look for dlt.yml or .dlt folder is found
    - if not, look recursively up from cwd() until, go to 1
    - stop looking when root folder dlt global dir (home dir) is reached and return cwd

    Returns project dir
    """

    cwd = current_dir = os.getcwd()
    root_dir = os.path.abspath(os.sep)  # platform-independent root directory
    dlt_global_dir = os.path.dirname(global_dir())

    while True:
        if current_dir == dlt_global_dir:
            # Reached global dir (ie. home directory), end of search
            return cwd
        if is_project_dir(current_dir):
            return current_dir
        if pyproject_dir := find_pyproject_project_dir(current_dir):
            return pyproject_dir
        if current_dir == root_dir:
            # Reached the root directory without finding the file
            return None
        # Move up one directory level
        current_dir = os.path.dirname(current_dir)


def is_project_dir(project_dir: str) -> bool:
    """Checks if `project_dir` contains dlt project, this is true if a config file is found"""
    if os.path.isfile(os.path.join(project_dir, DEFAULT_PROJECT_CONFIG_FILE)):
        return True
    # if os.path.isdir(os.path.join(project_dir, DOT_DLT)):
    #     return True
    return False


def ensure_project(run_dir: str = None, profile: str = None) -> ProjectRunContext:
    # TODO: remove the context switching, just return current context
    # gets current run context, optionally switching to an alternative run_dir or profile
    from dlt.common.runtime.run_context import current

    if run_dir:
        # switch project in explicit path
        context: SupportsRunContext = switch_context(run_dir, profile)
    elif profile:
        # only switch profile
        context = switch_profile(profile)
    else:
        context = current()
    if not isinstance(context, ProjectRunContext):
        raise ProjectRunContextNotAvailable(context.run_dir, context)

    return context


def list_dlt_packages() -> List[InstalledDltPackageInfo]:
    """Lists Python packages that contain modules with dlt packages.
    Returns list of tuples (package name, module name, first line of docstring)
    """
    import importlib.metadata
    from dlt.cli import echo as fmt

    packages: List[InstalledDltPackageInfo] = []
    for dist in importlib.metadata.distributions():
        package_name = dist.metadata.get("Name")
        if not package_name:
            continue

        entry_points = dist.entry_points

        # try to read package info
        package_info: InstalledDltPackageInfo = None
        license_scopes: str = None
        # filter entry points under 'dlt_package'
        dlt_package_eps = [ep for ep in entry_points if ep.group == "dlt_package"]
        if dlt_package_eps:
            for ep in dlt_package_eps:
                if ep.name == "dlt-project":
                    module_name = ep.value
                    try:
                        module = importlib.import_module(module_name)
                        # get the module-level docstring
                        docstring = module.__doc__ or ""
                        fl = docstring.strip().split("\n")[0]
                        package_info = InstalledDltPackageInfo(package_name, module_name, fl)
                    except Exception as e:
                        fmt.error(f"Error processing {package_name}, module {module_name}: {e}")
                elif ep.name == "license-scopes":
                    license_scopes = ep.value
        if package_info:
            package_info.license_scopes = license_scopes
            packages.append(package_info)
    return packages


def project_from_args(args: argparse.Namespace) -> ProjectRunContext:
    if args.project and not os.path.exists(args.project):
        import importlib

        try:
            module = importlib.import_module(args.project)
            args.project = os.path.dirname(os.path.abspath(module.__file__))
        except ImportError:
            pass
    return ensure_project(args.project, profile=args.profile)
