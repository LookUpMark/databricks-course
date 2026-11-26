"""Unit tests for playbook.context."""

from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from playbook.config import load_settings
from playbook.context import JobContext, resolve_context
from playbook.utils.cli_parser import JobArgs

PACKAGED_CONFIG = Path(__file__).resolve().parents[3] / "src" / "playbook" / "config"


def test_resolve_context_uses_explicit_arguments():
    settings = load_settings(PACKAGED_CONFIG)
    context = resolve_context(JobArgs(catalog="main", schema="sales"), settings)
    assert context == JobContext(catalog="main", schema="sales")


def test_resolve_context_strips_whitespace_and_accepts_simple_identifiers():
    settings = load_settings(PACKAGED_CONFIG)
    context = resolve_context(JobArgs(catalog="  Main_2 ", schema="\t_course1\n"), settings)
    assert context == JobContext(catalog="Main_2", schema="_course1")


@pytest.mark.parametrize(
    "args",
    [
        JobArgs(catalog="", schema="sales"),
        JobArgs(catalog="main", schema=" "),
        JobArgs(catalog="training-data", schema="sales"),
        JobArgs(catalog="main", schema="2sales"),
        JobArgs(catalog="main", schema="sales.archive"),
        JobArgs(catalog="main", schema="sales`"),
    ],
)
def test_resolve_context_rejects_invalid_identifiers(args):
    with pytest.raises(ValueError, match="simple Unity Catalog identifiers"):
        resolve_context(args, load_settings(PACKAGED_CONFIG))


def test_resolve_context_is_frozen():
    settings = load_settings(PACKAGED_CONFIG)
    context = resolve_context(JobArgs(catalog="main", schema="sales"), settings)
    with pytest.raises(FrozenInstanceError):
        context.catalog = "other"
