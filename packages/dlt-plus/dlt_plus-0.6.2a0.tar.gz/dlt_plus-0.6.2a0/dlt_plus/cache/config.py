from typing import Dict, Optional, List, Union
from typing_extensions import TypedDict

import os

from dlt.common.schema.typing import TWriteDisposition
from dlt.common.validation import validate_dict
from dlt.destinations.dataset import ReadableDBAPIDataset


class CacheBinding(TypedDict, total=False):
    dataset: Union[ReadableDBAPIDataset, str]
    tables: Optional[Dict[str, str]]


class CacheInputBinding(CacheBinding):
    pass


class CacheOutputBinding(CacheBinding):
    write_disposition: Optional[TWriteDisposition]
    loader_file_format: Optional[str]


class CacheConfig(TypedDict, total=False):
    name: Optional[str]
    type: Optional[str]
    location: Optional[str]
    pipeline_name: Optional[str]
    dataset_name: Optional[str]
    transformed_dataset_name: Optional[str]
    inputs: List[CacheInputBinding]
    outputs: List[CacheOutputBinding]


def set_defaults_and_validate(config: CacheConfig) -> CacheConfig:
    # set some defaults
    # TODO: transformation should keep the cache dir using the same mechanism as pipeline
    # it should support SupportsPipeline protocol
    import dlt

    config.setdefault("location", dlt.current.run_context().data_dir)
    config.setdefault("type", "duckdb")
    config.setdefault("pipeline_name", config["name"] + "_cache")
    config.setdefault("dataset_name", config["name"] + "_cache_dataset")
    config.setdefault(
        "transformed_dataset_name",
        config["dataset_name"] + "_transformed",
    )

    # always keep location as abspath.
    config["location"] = os.path.abspath(os.path.join(config["location"]))

    validate_dict(CacheConfig, config, ".")

    return config
