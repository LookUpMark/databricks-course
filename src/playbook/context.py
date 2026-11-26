"""Execution context resolution.

Validate CLI arguments and return the effective Unity Catalog context.
This module requires no Databricks runtime.
"""

import re
from dataclasses import dataclass

from playbook.config import Settings
from playbook.utils.cli_parser import JobArgs


@dataclass(frozen=True)
class JobContext:
    """Effective Unity Catalog context for a run.

    Attributes:
        catalog: Catalog to activate for the run.
        schema: Schema inside ``catalog`` to activate.
    """

    catalog: str
    schema: str


def resolve_context(args: JobArgs, settings: Settings) -> JobContext:
    """Resolve the effective Unity Catalog context from explicit arguments.

    Args:
        args: Arguments parsed from the command line.
        settings: Validated project settings, retained for interface compatibility.

    Returns:
        The context to apply before running any data operation.

    Raises:
        ValueError: If either argument is not a simple Unity Catalog identifier.
    """
    catalog, schema = args.catalog.strip(), args.schema.strip()
    if not all(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part) for part in (catalog, schema)):
        raise ValueError("Set catalog and schema to simple Unity Catalog identifiers before running the job.")
    return JobContext(catalog=catalog, schema=schema)
