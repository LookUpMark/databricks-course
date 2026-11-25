# Third-party notices

[MIT](LICENSE) applies to original contributions in this repository. The parts derived from Databricks' `default-python` bundle template are distributed under the [Databricks License](licenses/Databricks.txt). Copyright (2022) Databricks, Inc. See the [upstream notice](https://github.com/databricks/cli/blob/v1.21.0/NOTICE) for Databricks' attribution. The Databricks CLI and its dependencies are installed separately.

The [upstream template](https://github.com/databricks/cli/tree/v1.21.0/libs/template/templates/default-python) supplied the initial bundle and example structure. The following files retain or adapt that work:

- `databricks.yml`, `resources/sample_job.job.yml`, and `resources/playbook_etl.pipeline.yml`. The bundle targets a learner's OAuth profile and catalog/schema, and the resource paths and tasks were adapted for the course.
- `src/sample_notebook.py` and `src/playbook_etl/transformations/`. The sample notebook was converted to the Databricks source format and validates widgets. The pipeline functions use the Lakeflow Python API and retain the sample taxi workload.
- The template portions of `src/playbook/__init__.py`, `src/playbook/main.py`, `src/playbook/taxis.py`, `tests/integration/conftest.py`, and `tests/integration/playbook/test_taxis.py` were moved or adapted for the course's package and test layout.
- `.gitignore`, `pyproject.toml`, and `uv.lock` were adapted or generated for this repository's code and dependency versions.

The examples reference the Databricks `samples.nyctaxi.trips` dataset in the learner's workspace. This repository does not distribute that dataset.
