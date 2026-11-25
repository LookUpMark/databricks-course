"""End-to-end test of the entry-point chain without a live Spark session.

Chain: CLI args -> validated settings -> resolved context, mirroring exactly
what ``playbook.main.run`` does before its first Spark call.
"""

from pathlib import Path

from playbook.config import load_settings
from playbook.context import resolve_context
from playbook.utils.cli_parser import parse_args

CONFIG_DIR = Path(__file__).resolve().parents[2] / "src" / "playbook" / "config"


def test_full_context_chain():
    args = parse_args(["--catalog", "main", "--schema", "sales"])
    settings = load_settings(CONFIG_DIR)
    context = resolve_context(args, settings)
    assert context.catalog == "main"
    assert context.schema == "sales"
