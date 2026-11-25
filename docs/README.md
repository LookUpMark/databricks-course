# Documentation index

This wiki mirrors the repository: one markdown file per source file, plus
project-level overviews. Read the overviews first, then dive into per-file guides.

## Overviews

- [Architecture](overview/architecture.md) — how the project fits together.
- [Pipelines](overview/pipelines.md) — end-to-end phases, files and methods.
- [Conventions](overview/conventions.md) — the rules this template enforces.

## Source mirror (`src/`)

| Source file | Documentation |
|---|---|
| `src/playbook/main.py` | [main.md](src/playbook/main.md) |
| `src/playbook/taxis.py` | [taxis.md](src/playbook/taxis.md) |
| `src/playbook/context.py` | [context.md](src/playbook/context.md) |
| `src/playbook/config/__init__.py` | [config-package.md](src/playbook/config/config-package.md) |
| `src/playbook/config/loader.py` | [loader.md](src/playbook/config/loader.md) |
| `src/playbook/config/models.py` | [models.md](src/playbook/config/models.md) |
| `src/playbook/config/settings.yaml` | [settings.md](src/playbook/config/settings.md) |
| `src/playbook/config/ml.yaml` | [ml.md](src/playbook/config/ml.md) |
| `src/playbook/config/etl.yaml` | [etl.md](src/playbook/config/etl.md) |
| `src/playbook/utils/logging.py` | [logging.md](src/playbook/utils/logging.md) |
| `src/playbook/utils/cli_parser.py` | [cli_parser.md](src/playbook/utils/cli_parser.md) |

## Tests mirror (`tests/`)

- `tests/unit/` mirrors `src/playbook/` one-to-one: a `test_<file>.py` for every
  module, no Spark or network dependencies.
- `tests/integration/` exercises function chains against a live Databricks
  connection (fixtures in `tests/integration/conftest.py`).
- `tests/e2e/` runs the full entry-point chain minus the live Spark calls.
