import os
from typing import Any, ClassVar, Dict, Iterable, List, Mapping, Optional, cast

import dlt
from dlt.common.configuration.providers import CustomLoaderDocProvider
from dlt.common.utils import exclude_keys

from dlt_plus.cache.config import CacheConfig

from ..exceptions import ProjectException
from .interpolation import InterpolateEnvironmentVariables
from .typing import (
    ProjectConfig,
    SourceConfig,
    DestinationConfig,
    PipelineConfig,
    DatasetConfig,
    ProfileConfig,
    ProjectSettingsConfig,
)


def select_keys(d: Mapping[str, Any], keys: Iterable[str]) -> Dict[str, Any]:
    return {key: d[key] for key in keys if key in d}


def exclude_keys_from_nested(data: Mapping[str, Any], keys: Iterable[str]) -> Dict[str, Any]:
    return {
        nested_key: {
            key: value if not isinstance(value, Mapping) else exclude_keys(value, keys)
            for key, value in nested_mapping.items()
        }
        for nested_key, nested_mapping in data.items()
        if nested_mapping
    }


class Project(Dict[str, Any]):
    DEFAULT_PROVIDER_NAME: ClassVar[str] = "dlt_project"
    # NOTE: the mechanism below is unclear at this point..
    KEYS_TO_EXCLUDE: ClassVar[List[str]] = ["profiles", "pipelines", "project"]
    TYPE_KEY: ClassVar[str] = "type"

    def __init__(
        self,
        config: ProjectConfig,
        settings: ProjectSettingsConfig,
        project_dir: str,
        profile_name: str,
    ):
        self.project_dir = project_dir

        self._raw_config = config
        self._settings = cast(
            ProjectSettingsConfig,
            {"project_dir": project_dir, **settings, "current_profile": profile_name},
        )
        # first interpolate project config with self
        interpolator = InterpolateEnvironmentVariables(extra_vars=dict(self.settings))
        self._settings = interpolator.interpolate(self._settings)  # type: ignore

        # then interpolate project config with pre interpolated settings
        interpolator = InterpolateEnvironmentVariables(extra_vars=dict(self.settings))
        interpolated_config = interpolator.interpolate(self._raw_config)  # type: ignore[arg-type]

        super().__init__(interpolated_config)

    @property
    def settings(self) -> ProjectSettingsConfig:
        return self._settings

    @property
    def current_profile(self) -> str:
        return self._settings["current_profile"]

    @property
    def name(self) -> str:
        return self._settings.get("name") or os.path.basename(self.project_dir)

    @property
    def tmp_dir(self) -> str:
        return self._settings.get("tmp_dir")

    @property
    def default_profile(self) -> str:
        return self._settings.get("default_profile")

    def provider(
        self, provider_name: Optional[str] = None, subset_keys: Optional[Iterable[str]] = None
    ) -> CustomLoaderDocProvider:
        provider_name = provider_name or self.DEFAULT_PROVIDER_NAME
        return CustomLoaderDocProvider(provider_name, lambda: self._preprocess(subset_keys))

    def register(
        self, provider_name: Optional[str] = None, subset_keys: Optional[Iterable[str]] = None
    ) -> None:
        dlt.config.register_provider(self.provider(provider_name, subset_keys))

    def _preprocess(self, subset_keys: Iterable[str] = None) -> Dict[str, Any]:
        if subset_keys:
            filtered = select_keys(self, subset_keys)
        else:
            filtered = self
        # this also clones the dictionary
        pipelines = filtered.get("pipelines")
        filtered = exclude_keys(filtered, self.KEYS_TO_EXCLUDE)
        # rename the destination to destinations
        if "destinations" in filtered:
            filtered["destination"] = filtered.pop("destinations")

        if filtered.get("destination"):
            # set duckdb database path to temp
            # TODO: move this to the core library, if the destination is named,
            #   use the name to create default duckdb location
            for destination_name, destination_config in filtered["destination"].items():
                if destination_config and destination_config.get("type") == "duckdb":
                    if not destination_config.get("credentials"):
                        destination_config["credentials"] = os.path.join(
                            self.tmp_dir, destination_name + ".duckdb"
                        )

        # convert pipelines into pipelines config
        if pipelines:
            filtered.update(pipelines)
        return exclude_keys_from_nested(filtered, {self.TYPE_KEY})

    @property
    def sources(self) -> Dict[str, SourceConfig]:
        return cast(Dict[str, SourceConfig], self.get("sources") or {})

    @property
    def destinations(self) -> Dict[str, DestinationConfig]:
        return cast(Dict[str, DestinationConfig], self.get("destinations") or {})

    @property
    def profiles(self) -> Dict[str, ProfileConfig]:
        return cast(Dict[str, ProfileConfig], self.get("profiles") or {})

    @property
    def pipelines(self) -> Dict[str, PipelineConfig]:
        return cast(Dict[str, PipelineConfig], self.get("pipelines") or {})

    @property
    def transformations(self) -> Dict[str, Any]:
        return cast(Dict[str, Any], self.get("transformations") or {})

    @property
    def caches(self) -> Dict[str, CacheConfig]:
        return cast(Dict[str, CacheConfig], self.get("caches") or {})

    @property
    def datasets(self) -> Dict[str, DatasetConfig]:
        return cast(Dict[str, DatasetConfig], self.get("datasets") or {})

    def resolve_dataset_destinations(self, dataset_name: str) -> List[str]:
        """Infers possible destinations from the pipelines if not explicitly limited"""
        dataset_config = self.datasets.get(dataset_name) or {}
        available_destinations = dataset_config.get("destination")

        # if no explicit destinations, take them from defined pipelines
        # TODO: move this to entity manager so we can also check dataseta and pipleine
        # not explicitly defined in config
        if available_destinations is None:
            available_destinations = []
            for pipeline_config in self.pipelines.values():
                if pipeline_config:
                    if dataset_name == pipeline_config.get("dataset_name"):
                        if destination_name := pipeline_config.get("destination"):
                            available_destinations.append(destination_name)

        if not available_destinations:
            raise ProjectException(
                self.project_dir,
                f"Destination(s) are not specified for dataset '{dataset_name}' and cannot be "
                "inferred from pipelines. Please use `destination` property to define a list of "
                "destinations where dataset may be present.",
            )
        return list(set(available_destinations))
