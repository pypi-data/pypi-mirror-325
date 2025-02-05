from typing import Optional, Union

from typing_extensions import TypedDict

from dlt.common.validation import validate_dict

from dlt_plus.cache.cache import Cache


class TransformationConfig(TypedDict, total=False):
    name: str
    engine: str
    package_name: str
    location: Optional[str]
    cache: Union[str, Cache]


def set_defaults_and_validate(config: TransformationConfig) -> TransformationConfig:
    # set some defaults
    # TODO: transformation should keep the cache dir using the same mechanism as pipeline
    # it should support SupportsPipeline protocol

    # always keep location as abspath.
    config.setdefault("engine", "dbt")
    engine = config["engine"]
    config.setdefault("package_name", engine + "_" + config["name"])

    validate_dict(TransformationConfig, config, ".")
    return config
