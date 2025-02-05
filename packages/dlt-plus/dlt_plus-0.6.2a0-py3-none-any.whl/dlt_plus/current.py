from typing import Optional

from dlt_plus.project.catalog import Catalog
from dlt_plus.project.config.config import Project
from dlt_plus.project.entity_factory import EntityFactory
from dlt_plus.project.pipeline_manager import PipelineManager
from dlt_plus.project.run_context import ProjectRunContext, ensure_project


def context(profile: Optional[str] = None) -> ProjectRunContext:
    """Returns the context of current project, including run directory,
    data directory and project config
    """
    return ensure_project(profile=profile)


def project(context_: ProjectRunContext = None) -> Project:
    """Returns project configuration and getters of entities like sources, destinations
    and pipelines"""
    return (context_ or context()).config


def entities(context_: ProjectRunContext = None) -> EntityFactory:
    """Returns methods to create entities in this package likes sources, pipelines etc."""
    return EntityFactory(project(context_))


def runner(context_: ProjectRunContext = None) -> PipelineManager:
    return PipelineManager(project(context_))


def catalog(context_: ProjectRunContext = None) -> Catalog:
    """Returns a catalogue with available datasets, which can be read and written to"""
    return Catalog(context_ or context())
