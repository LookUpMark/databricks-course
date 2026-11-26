# src/playbook/context.py

Resolves the effective Unity Catalog context for a run. Pure module: no
runtime imports, trivially unit-testable.

## Dataclass

`JobContext(frozen=True)` with fields `catalog: str` and `schema: str`.
Frozen by design: once resolved, the context cannot be mutated accidentally by
downstream code — the same immutability guarantee as `JobArgs`.

## Functions

### `resolve_context(args: JobArgs, settings: Settings) -> JobContext`

Single chain step from "what the user asked" to "what the job will use".

1. Reads and trims `args.catalog` and `args.schema`.
2. Validates both names against `[A-Za-z_][A-Za-z0-9_]*` and raises `ValueError` for invalid values.
3. Returns a frozen `JobContext` containing the validated names.

The `settings` argument is retained for interface compatibility. The job requires both CLI arguments.

## Interactions

- Called by: `main.py::run`.
- Depends on: `JobArgs` (from `utils.cli_parser`), `Settings` (from `config`),
  both as injected values.
- Tests: `tests/unit/playbook/test_context.py` — explicit arguments, trimming, validation, and immutability.
