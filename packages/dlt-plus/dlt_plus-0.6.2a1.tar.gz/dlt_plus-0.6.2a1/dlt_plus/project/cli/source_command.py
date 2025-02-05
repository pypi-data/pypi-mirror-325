import argparse
import importlib

from dlt.cli import SupportsCliCommand
from dlt.cli import echo as fmt

from .helpers import add_source
from dlt_plus.common.cli import add_project_opts

from ..run_context import ProjectRunContext
from dlt_plus.project.cli.helpers import project_from_args_with_cli_output
from dlt_plus.common.license import require_license
from .formatters import print_entity_list


class SourceCommand(SupportsCliCommand):
    command = "source"
    help_string = "Manage dlt+ project sources"
    description = """
Commands to manage sources for project.
Run without arguments to list all sources in current project.
"""

    def configure_parser(self, parser: argparse.ArgumentParser) -> None:
        self.parser = parser

        add_project_opts(parser)

        parser.add_argument("source_name", help="Name of the source to add.", nargs="?")

        subparsers = parser.add_subparsers(title="Available subcommands", dest="source_command")

        subparsers.add_parser(
            "check",
            help="(temporary feature) Checks if the source is importable, only works for "
            + "sources within the sources folder.",
            description="(temporary feature) Checks if the source is importable, only works for "
            + "sources within the sources folder.",
        )

        subparsers.add_parser(
            "list",
            help="List all sources in the project.",
            description="""
List all sources in the project context.
""",
        )

        add_parser = subparsers.add_parser(
            "add",
            help="Add a new source to the project.",
            description="""
Add a new source to the project context.

* If source type is not specified, the source type will be the same as the source name.
* If a give source_type is not found, a default source template will be used.
""",
        )
        add_parser.add_argument(
            "source_type",
            help="Type of the source to add. If not specified, "
            "the source type will be the same as the source name.",
            nargs="?",
        )

    @require_license(scope="dlt_plus.project")
    def execute(self, args: argparse.Namespace) -> None:
        project_run_context = project_from_args_with_cli_output(args)

        if args.source_command == "add":
            add_project_source(project_run_context, args.source_name, args.source_type)
        elif args.source_command == "list":
            print_entity_list(
                "source",
                [
                    f"{name}: {config.get('type')}"
                    for name, config in project_run_context.config.get("sources", {}).items()
                ],
            )
        elif args.source_command == "check":
            check_project_source(project_run_context, args.source_name)
        else:
            self.parser.print_usage()


def add_project_source(
    project_run_context: ProjectRunContext, source_name: str, source_type: str
) -> None:
    fmt.echo("Will add a new source to your dlt+ project.")
    if not fmt.confirm("Do you want to proceed?", default=True):
        exit(0)
    add_source(project_run_context, source_name, source_type)


def check_project_source(project_run_context: ProjectRunContext, source_name: str) -> None:
    fmt.echo(f"Checking if source {source_name} is importable...")
    source_type = project_run_context.config.get("sources", {}).get(source_name, {}).get("type")
    if not source_type:
        fmt.error(f"Source {source_name} is not found in the project or has no type defined.")
        exit(1)

    # split source_type
    source_type_parts = source_type.split(".")
    if len(source_type_parts) <= 2:
        fmt.error(
            f"Source type {source_type} is not valid. Must be a valid "
            + "python module path in the sources module."
        )
        exit(1)

    source_module_path = ".".join(source_type_parts[:-1])
    importlib.import_module(source_module_path)

    fmt.note(f"Source file at {source_module_path} could be imported successfully.")
