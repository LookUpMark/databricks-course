# Tests

These optional developer checks cover the demonstration [Python package](../src/playbook/README.md). The course notebooks run in Databricks.

From the repository root, install the locked developer dependencies and run the offline suite (also selected by `uv run pytest`):

```bash
uv sync --locked --dev
uv run pytest tests/unit tests/e2e
```

- `unit/` exercises package configuration, argument parsing and context without networking.
- `e2e/` checks the entry-point chain with a stand-in for Spark.
- `integration/` connects to a live Databricks workspace. Configure a Databricks profile and compute compatible with the Databricks Connect version in [pyproject.toml](../pyproject.toml), and ensure access to `samples.nyctaxi.trips`. Run `uv run pytest tests/integration` only when you intend to use that compute. The project pins Databricks Connect to the 16.4 series with Python 3.12. The [compatibility matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements) lists Databricks Runtime 16.4 for clusters and serverless environment 3 for Connect 16.4.1 and later in that series. The deployed Python wheel task uses its own serverless environment 5.
