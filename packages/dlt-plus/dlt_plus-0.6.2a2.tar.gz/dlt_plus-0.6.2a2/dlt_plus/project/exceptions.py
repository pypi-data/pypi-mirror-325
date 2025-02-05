import os
from typing import Iterable

from dlt.common.configuration.specs.pluggable_run_context import SupportsRunContext
from dlt.common.runtime.exceptions import RuntimeException

from dlt_plus.common.exceptions import DltPlusException


class ProjectException(DltPlusException):
    def __init__(self, project_dir: str, msg: str):
        self.project_dir = project_dir
        super().__init__(msg)


class ProjectRunContextNotAvailable(ProjectException, RuntimeException):
    def __init__(self, project_dir: str, existing_context: SupportsRunContext):
        self.existing_context = existing_context
        msg = (
            f"A dlt project could not be found for path {os.path.abspath(project_dir)}. "
            "A lookup for a dlt.yml file failed for this and any parent path. "
            "A Python project (pyproject.toml) defining Python package with dlt project was "
            "not found at this path."
        )
        super().__init__(project_dir, msg)


class ProjectDocValidationError(ProjectException):
    def __init__(self, project_dir: str, validation_err: str):
        super().__init__(
            project_dir,
            f"Project file {project_dir} contains unknown or invalid entities: {validation_err}",
        )


class ProfileNotFound(ProjectException, KeyError):
    def __init__(self, project_dir: str, profile_name: str, available_profiles: Iterable[str]):
        super().__init__(
            project_dir,
            f"Project {project_dir} does not declare profile {profile_name}"
            f" and {profile_name} is not one of implicit profiles. "
            f"Available profiles: {available_profiles}",
        )


class ProjectExplicitEntityNotFound(ProjectException, KeyError):
    """Explicitly defined `entity` with `name` not found in project."""

    def __init__(self, project_dir: str, entity: str, name: str):
        self.entity = entity
        self.name = name
        super().__init__(
            project_dir,
            f"{entity} with name '{name}' is not explicitly declared in project {project_dir} and "
            f"project settings (allow_undefined_entities) prevent undefined {entity} "
            "to be used.",
        )
