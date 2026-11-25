# playbook Python package

The course bundle builds this package as a Python wheel. The `python_wheel_task` in [sample_job](../../resources/sample_job.job.yml) installs it and calls the `main` entry point. It is a working part of [topic 09](../../course/09-lakeflow-jobs/LESSON.md).

| Module | Purpose |
|---|---|
| `main.py` | Parses job arguments, selects the schema, and previews the sample NYC taxi data. |
| `context.py` | Resolves job arguments against package defaults. |
| `taxis.py` | Reads `samples.nyctaxi.trips` using an injected Spark session. |
| `config/` | Loads YAML and validates it with Pydantic. The bundle passes catalog and schema explicitly. |
| [utils/](utils/README.md) | CLI parsing and logging with Loguru. |

See the [developer docs](../../docs/README.md) for individual modules and [tests](../../tests/README.md) for local verification.
