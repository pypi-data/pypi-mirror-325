from typing import Dict, Any, cast

import dlt
import os
from contextlib import contextmanager

from dlt import Pipeline, Schema
from dlt.common import logger
from dlt.common.exceptions import DltException, MissingDependencyException
from dlt.common.destination.dataset import SupportsReadableRelation

from dlt.destinations import duckdb as duckdb_destination
from dlt.destinations.exceptions import DatabaseUndefinedRelation
from dlt.destinations.dataset import ReadableDBAPIDataset
from dlt.destinations.impl.filesystem.filesystem import FilesystemClient

try:
    from dlt.destinations.impl.filesystem.sql_client import FilesystemSqlClient
except ImportError as import_ex:
    from dlt_plus import version

    raise MissingDependencyException(
        "transformations and local cache",
        [f"{version.PKG_NAME}[cache]"],
        "Install extras above to run local cache and transformations",
    ) from import_ex

from dlt_plus.cache.config import (
    CacheConfig,
    CacheInputBinding,
    set_defaults_and_validate,
    CacheBinding,
)


def create_cache(config: CacheConfig) -> "Cache":
    return Cache(config)


class CacheException(DltException):
    pass


class Cache:
    """A duckdb backed cache for working on data locally"""

    def __init__(self, config: CacheConfig) -> None:
        self.config = set_defaults_and_validate(config)

    def populate(self) -> None:
        """load data from the connected input datasets into cache"""
        # NOTE: At this moment only filesystem view mounts are supported
        self.verify_inputs()

        # collect datasets to load
        # tables_to_copy: Dict[str, SupportsReadableRelation] = {}
        for cache_input in self.config["inputs"]:
            # filesystem destination tables can be mounted as views in most cases
            with self._get_fs_sql_client_for_input(cache_input) as sql_client:
                sql_client.create_views_for_tables(self._get_tables_for_input(cache_input))

        # NOTE: the below currently will not run ever,
        # as we are just linking filesystem views for now
        # later we can also copy data into the cache
        # for in_table, out_table in cache_input["tables"].items():
        #    tables_to_copy[out_table] = input_pipeline.dataset()[in_table]

        # @dlt.source()
        # def in_source():
        #     for name, dataset in tables_to_copy.items():
        #         yield dlt.resource(
        #             dataset.iter_arrow(500),
        #             name=name,
        #             write_disposition="replace",
        #         )

        # cache_pipeline.run(in_source())

    #
    # Outputs
    #
    def flush(self) -> None:
        """Flushes the results into the connected output datasets"""
        self.verify_outputs()

        cache_pipeline = self.get_cache_pipeline(transformed_data=True)
        for cache_output in self.config["outputs"]:
            # sync result tables into output dataset
            data: Dict[str, SupportsReadableRelation] = {}

            for in_table, out_table in cache_output["tables"].items():
                data[out_table] = cache_pipeline.dataset()[in_table]

            @dlt.source()
            def out_source() -> Any:
                for name, dataset in data.items():
                    yield dlt.resource(
                        dataset.iter_arrow(50000), name=name, write_disposition="append"
                    )

            output_pipeline = self.get_binding_pipeline(cache_output)
            output_pipeline.run(
                out_source(),
                loader_file_format=cache_output.get("loader_file_format", None),  # type: ignore
            )

    def verify_outputs(self) -> None:
        """checks that we have tables for all defined output tables"""

        if len(self.config["outputs"]) != 1:
            raise CacheException("Currently only one output is supported.")

        cache_pipeline = self.get_cache_pipeline(transformed_data=True)
        for cache_output in self.config["outputs"]:
            for table in cache_output["tables"].keys():
                try:
                    cache_pipeline.dataset()[table].fetchone()
                except DatabaseUndefinedRelation:
                    raise Exception(
                        f"Table {table} defined in output "
                        + f"{self.get_binding_pipeline(cache_output).dataset_name} does "
                        + "not exist in transformed dataset."
                    )

    #
    # Inputs
    #
    def verify_inputs(self) -> None:
        """connect to each input and verify specified tables exist in schema"""

        if len(self.config["inputs"]) != 1:
            raise CacheException("Currently only one input is supported.")

        for cache_input in self.config["inputs"]:
            input_dataset = self.get_binding_dataset(cache_input)
            assert input_dataset.schema
            for table in (cache_input.get("tables") or {}).keys():
                if not input_dataset[table].columns_schema:
                    raise Exception(
                        f"Table {table} doesn't exist in the input of "
                        + f"pipeline {input_dataset._dataset_name}"
                    )

    def discover_input_schema(self) -> Schema:
        """Sync all inputs and calculate the input schema"""
        self.verify_inputs()
        schema = Schema(self.config["pipeline_name"])
        for cache_input in self.config["inputs"]:
            input_dataset = self.get_binding_dataset(cache_input)
            for in_table, out_table in self._get_tables_for_input(cache_input).items():
                schema.tables[out_table] = input_dataset.schema.tables[in_table]

        return schema

    def _get_tables_for_input(self, cache_input: CacheInputBinding) -> Dict[str, str]:
        input_dataset = self.get_binding_dataset(cache_input)
        tables = cache_input.get("tables") or {}

        # no tables declared means sync all data tables
        if not tables:
            for t in input_dataset.schema.data_tables():
                tables[t["name"]] = t["name"]

        # add load id table
        tables[input_dataset.schema.loads_table_name] = input_dataset.schema.loads_table_name

        return tables

    #
    # Cache management
    #
    def drop(self) -> None:
        self.drop_input_dataset()
        self.drop_output_dataset()

    def drop_input_dataset(self) -> None:
        try:
            p = self.get_cache_pipeline(False)
            with p.sql_client() as sql_client:
                sql_client.drop_dataset()
            logger.info(f"Dataset {p.dataset_name} deleted")
        except DatabaseUndefinedRelation:
            logger.info(f"Cache input dataset {p.dataset_name} does not exist. Nothing to do.")

    def drop_output_dataset(self) -> None:
        try:
            p = self.get_cache_pipeline(True)
            with p.sql_client() as sql_client:
                sql_client.drop_dataset()
            logger.info(f"Dataset {p.dataset_name} deleted")
        except DatabaseUndefinedRelation:
            logger.info(f"Cache output dataset {p.dataset_name} does not exist. Nothing to do.")

    def wipe(self) -> None:
        """Destroys all local data (cache, pipelines) of the cache"""
        p = self.get_cache_pipeline(False)
        p._wipe_working_folder()
        p = self.get_cache_pipeline(True)
        p._wipe_working_folder()
        if os.path.exists(self.cache_location):
            os.remove(self.cache_location)

    #
    # Managing secrets
    #
    @contextmanager
    def with_persistent_secrets(self) -> Any:
        try:
            self.create_persistent_secrets()
            yield
        finally:
            self.clear_persistent_secrets()

    def secret_name_for_input(self, p: CacheInputBinding) -> str:
        dataset = self.get_binding_dataset(p)
        return f"cache_secrets_{self.config['name']}_{dataset._dataset_name}"

    def create_persistent_secrets(self) -> None:
        for cache_input in self.config["inputs"]:
            with self._get_fs_sql_client_for_input(cache_input) as sql_client:
                try:
                    sql_client.create_authentication(
                        persistent=True, secret_name=self.secret_name_for_input(cache_input)
                    )
                except Exception:
                    pass

    def clear_persistent_secrets(self) -> None:
        import duckdb

        for cache_input in self.config["inputs"]:
            with self._get_fs_sql_client_for_input(cache_input) as sql_client:
                try:
                    sql_client.drop_authentication(
                        secret_name=self.secret_name_for_input(cache_input)
                    )
                except duckdb.InvalidInputException:
                    pass

    def get_cache_input_dataset(self) -> ReadableDBAPIDataset:
        return cast(ReadableDBAPIDataset, self.get_cache_pipeline(transformed_data=False).dataset())

    def get_cache_output_dataset(self) -> ReadableDBAPIDataset:
        return cast(ReadableDBAPIDataset, self.get_cache_pipeline(transformed_data=True).dataset())

    @property
    def cache_location(self) -> str:
        """Returns the cache location ie. duckdb path"""
        cache_db_name = self.config["name"] + "_cache.duckdb"
        return os.path.join(self.config["location"], cache_db_name)

    def get_cache_pipeline(self, transformed_data: bool = False) -> Pipeline:
        dataset_name = (
            self.config["transformed_dataset_name"]
            if transformed_data
            else self.config["dataset_name"]
        )
        # TODO: place cache location in transformation working dir
        # (same concept as pipeline working dir!)
        return dlt.pipeline(
            self.config["pipeline_name"],
            destination=duckdb_destination(credentials=self.cache_location),
            dataset_name=dataset_name,
        )

    def get_binding_pipeline(self, o: CacheBinding) -> Pipeline:
        # TODO: make this unique per output or something, not sure
        dataset = self.get_binding_dataset(o)
        pipeline_name = "cache_" + dataset._dataset_name + "_output"
        return dlt.pipeline(
            pipeline_name=pipeline_name,
            destination=dataset._destination,
            dataset_name=dataset._dataset_name,
        )

    #
    # Private helpers
    #
    def get_binding_dataset(self, i: CacheBinding) -> ReadableDBAPIDataset:
        dataset = i.get("dataset")
        if isinstance(dataset, ReadableDBAPIDataset):
            return dataset
        raise Exception(f"Dataset {dataset} is not a valid dataset or unresolved dataset")

    def _get_fs_sql_client_for_input(self, cache_input: CacheInputBinding) -> FilesystemSqlClient:
        input_dataset = self.get_binding_dataset(cache_input)
        fs_client = input_dataset._destination_client(input_dataset.schema)

        if not isinstance(fs_client, FilesystemClient):
            in_dest = input_dataset._destination.destination_type
            raise CacheException(
                "Currently only filesystem inputs are supported. "
                f"Dataset {input_dataset._dataset_name} is not a filesystem input but a "
                f"{in_dest}."
            )
        cache_pipeline = self.get_cache_pipeline()
        return FilesystemSqlClient(
            dataset_name=cache_pipeline.dataset_name,
            fs_client=fs_client,
            credentials=cache_pipeline.destination_client().config.credentials,  # type: ignore
        )
