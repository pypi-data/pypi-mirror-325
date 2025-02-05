from typing import Any, List, Dict, Optional
from typing_extensions import TypedDict

from dlt.common.schema.typing import TSchemaContract

from dlt_plus.cache.config import CacheConfig


# TODO: generate project typedicts from existing SPECs (dataclasses) and extend them if needed
# some of the configurations are dynamic and generated from signatures (ie. sources, destinations)
# for those we won't be able to generate typedicts fully but maybe we will be able to
# generate JSON SCHEMA
# and use this for validation. We can also extend our validator with custom

# TODO: all sources are derived from BaseConfiguration with `with_args`
# corresponding to SourceFactory protocol
#   source specific params are taken from source signature and not known in advance
#   we have an option to put those in a separate property ie
# github:
#  args: {}
#  type
SourceConfig = Dict[str, Any]
# TODO: all destinations are derived from DestinationClientConfiguration,
# we can use UNION to represent known
# destinations or put the dynamic part into args.
DestinationConfig = Dict[str, Any]


class ProjectSettingsConfigBase(TypedDict, total=False):
    """Project settings in Config"""

    default_profile: Optional[str]
    tmp_dir: Optional[str]
    allow_undefined_entities: Optional[bool]


class ProjectSettingsConfig(ProjectSettingsConfigBase, total=False):
    """Project settings in Config"""

    name: Optional[str]
    # TODO: below split to internal class, those should not be validated!
    project_dir: Optional[str]
    current_profile: Optional[str]
    """not to be set in config"""


# TODO: generate and extend from PipelineConfiguration
class PipelineConfig(TypedDict, total=False):
    source: Optional[str]
    destination: str
    dataset_name: Optional[str]


class DatasetConfig(TypedDict, total=False):
    destination: Optional[List[str]]
    contract: Optional[TSchemaContract]


# TODO: we have several SPECs to add here: RUNTIME, NORMALIZE, LOAD, SCHEMA. all of them
#   must be derived from relevant SPECs.
class ProjectConfigBase(TypedDict, total=False):
    sources: Optional[Dict[str, Optional[SourceConfig]]]
    destinations: Optional[Dict[str, Optional[DestinationConfig]]]
    pipelines: Optional[Dict[str, PipelineConfig]]
    datasets: Optional[Dict[str, DatasetConfig]]
    caches: Optional[Dict[str, CacheConfig]]
    runtime: Optional[Dict[str, Any]]
    transformations: Optional[Any]


class ProfileConfig(ProjectConfigBase, total=False):
    project: Optional[ProjectSettingsConfigBase]


class ProjectConfig(ProjectConfigBase, total=False):
    profiles: Optional[Dict[str, Optional[ProfileConfig]]]
    project: Optional[ProjectSettingsConfig]
