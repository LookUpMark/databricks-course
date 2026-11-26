# src/playbook/utils/

Shared package utilities.

## Modules

- [logging.py](logging.py) configures Loguru format and level and writes to `stderr`.
- [cli_parser.py](cli_parser.py) uses `argparse` to read job arguments.

## Conventions

- One responsibility per module; no business logic here, only tooling.
- Every public function must have type hints and a docstring.
- Modules here must be importable both locally (tests) and on Databricks
  clusters (package wheel).
