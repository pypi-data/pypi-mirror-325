import dlt

from dlt_plus.transformations.base_transformation import Transformation
from dlt_plus.dbt_generator.render import Config, render_dbt_project, render_mart

ALLOWED_DBT_VERSION = ">=1.5,<1.8.9"


class DbtTransformation(Transformation):
    def render_transformation_layer(self, force: bool = False) -> None:
        """Renders a starting point for the t-layer"""
        schema = self.cache.discover_input_schema()
        cache_pipeline = self.cache.get_cache_pipeline()
        config = Config()
        config.base_folder = self.ponds_path
        config.render_readme_file = False
        config.render_run_script = False
        config.package_name = self.config["package_name"]
        config.update_from_pipeline(cache_pipeline, schema)
        config.force = force
        render_dbt_project(config)
        render_mart(config)

    def _do_transform(self) -> None:
        cache_pipeline = self.cache.get_cache_pipeline()
        venv = dlt.dbt.get_venv(cache_pipeline, dbt_version=ALLOWED_DBT_VERSION)
        dbt = dlt.dbt.package(cache_pipeline, self.transformation_layer_path, venv=venv)

        # run transformations
        dbt.run_all(
            # add any additional vars you need in dbt here
            additional_vars={},
            # change this to save your transformation results into another dataset
            destination_dataset_name=self.cache.config["transformed_dataset_name"],
        )
