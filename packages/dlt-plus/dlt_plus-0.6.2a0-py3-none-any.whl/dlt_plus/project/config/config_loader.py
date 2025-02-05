import os
from typing import Any, Dict, Optional, Set, Tuple, cast

from dlt.common.validation import validate_dict, DictValidationException

from dlt_plus.common.constants import DEFAULT_PROJECT_CONFIG_PROFILE, DEFAULT_TEMP_DIR

from dlt_plus.project.exceptions import ProfileNotFound, ProjectDocValidationError
from dlt_plus.project.config.typing import ProfileConfig, ProjectSettingsConfig, ProjectConfig
from dlt_plus.project.config.config import Project
from dlt_plus.project.config import yaml_loader
from dlt_plus.project.config.utils import normalize_path, clone_dict_nested, update_dict_nested


IMPLICIT_PROFILES = ["tests", "access"]


class ConfigLoader:
    def __init__(self, project_dir: str, raw_config: Dict[str, Any]):
        if not project_dir:
            raise ValueError("Project directory is required")

        # run validation on raw config
        try:
            validate_dict(ProjectConfig, raw_config, ".")
        except DictValidationException as ex:
            raise ProjectDocValidationError(project_dir, str(ex)) from ex

        self.project_dir = project_dir
        # safe to assign to type, raw config validated
        self.raw_config: ProjectConfig = raw_config  # type: ignore[assignment]

    def get_project_settings(self) -> ProjectSettingsConfig:
        """Gets project settings from raw config and sets defaults.
        Returns a deep clone of the raw settings
        """

        # set sensible defaults
        settings = clone_dict_nested(
            cast(ProjectSettingsConfig, self.raw_config.get("project", None) or {})
        )
        settings["project_dir"] = normalize_path(self.project_dir)

        # set default tmp dir
        settings["tmp_dir"] = settings.get("tmp_dir", "${project_dir}" + DEFAULT_TEMP_DIR)

        # set default profile
        settings["default_profile"] = settings.get(
            "default_profile", DEFAULT_PROJECT_CONFIG_PROFILE
        )

        # validate settings
        try:
            validate_dict(ProjectSettingsConfig, settings, "./project")
        except DictValidationException as ex:
            raise ProjectDocValidationError(self.project_dir, str(ex)) from ex

        return settings

    def get_available_profiles(self, project_settings: ProjectSettingsConfig) -> Set[str]:
        # get all explicit profiles, add default profile and implicit
        profiles = set((self.raw_config.get("profiles") or {}).keys())
        profiles.add(project_settings["default_profile"])
        profiles.update(IMPLICIT_PROFILES)
        return profiles

    # def validate_config(self) -> None:
    #     """Validates raw_config by seeing if all profile variants can be loaded"""
    #     # TODO: this is IMO overkill. if raw config validates, then all else validates
    #     for profile_name in self.get_available_profiles:
    #         self.get_config(profile_name)

    def get_profile(
        self,
        project_settings: ProjectSettingsConfig,
        profile_name: Optional[str] = None,
    ) -> Tuple[str, ProfileConfig]:
        """Gets profile from raw config, will select default profile if not specified.
        Returns a deep clone of the raw profile
        """

        profile_name = profile_name or project_settings["default_profile"]
        available_profiles = self.get_available_profiles(project_settings)

        # raise if profile missing
        if profile_name not in available_profiles:
            raise ProfileNotFound(self.project_dir, profile_name, available_profiles)

        selected_profile = (self.raw_config.get("profiles") or {}).get(profile_name) or {}
        return profile_name, clone_dict_nested(selected_profile)

    def get_config(self, profile: Optional[str] = None) -> Project:
        # get project settings with defaults
        project_settings = self.get_project_settings()

        # get selected or default profile
        profile, profile_config = self.get_profile(project_settings, profile)

        # use clone to merge profile and settings - make sure raw_config is not modified
        merged_config: ProjectConfig = clone_dict_nested(self.raw_config)

        # merge project settings with defaults into config and merge profile into this
        # we do this so profiles may override project settings
        merged_config = update_dict_nested(merged_config, {"project": project_settings})
        merged_config = update_dict_nested(merged_config, profile_config)

        merged_project_settings = merged_config.pop("project")
        # normalize project settings again as they may be overridden from profile
        merged_project_settings["tmp_dir"] = normalize_path(merged_project_settings["tmp_dir"])
        merged_project_settings["project_dir"] = normalize_path(
            merged_project_settings["project_dir"]
        )

        project = Project(merged_config, merged_project_settings, self.project_dir, profile)

        # Validate the merged configuration
        # TODO: we must allow additional properties ie. runtime or normalizer settings
        # the right approach would be to preserve known props or ignore additional props
        # commented out because demo project does not load
        # validate_dict(ProjectConfig, merged_config, ".")
        # TODO: generate json schema to validate yaml and enable autocomplete in editors
        # https://medium.com/@alexmolev/boost-your-yaml-with-autocompletion-and-validation-b74735268ad7
        # it is pretty easy to find SPECs for all known configurations and
        # convert them into JSON schema

        return project

    @classmethod
    def from_file(cls, file_path: str) -> "ConfigLoader":
        config = yaml_loader.load_file(file_path)
        return cls(os.path.dirname(file_path), config)

    @classmethod
    def from_string(cls, project_dir: str, yaml_string: str) -> "ConfigLoader":
        config = yaml_loader.load_string(yaml_string)
        return cls(project_dir, config)

    @classmethod
    def from_dict(cls, project_dir: str, raw_config: Dict[str, Any]) -> "ConfigLoader":
        return cls(project_dir, raw_config)
