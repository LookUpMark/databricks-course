# Architecture

The repository has two parts. Learners open [course notebooks](../../course/README.md) in Databricks. The [Declarative Automation Bundle](../../databricks.yml) defines the job and pipeline used in topics 09 and 10.

## Bundle execution

1. The Databricks CLI uses your active profile and reads the destination Unity Catalog catalog and schema from the bundle variables.
2. On deploy, the CLI builds the wheel and syncs the notebook and pipeline sources. [Resource YAML](../../resources/README.md) declares the job and pipeline. Development mode prefixes their names and pauses the periodic trigger.
3. When you run `sample_job`, its [notebook](../../src/sample_notebook.py) reads catalog and schema widgets. On success, the wheel task calls `playbook.main:main` and the pipeline task refreshes `playbook_etl` in parallel.
4. The wheel entry point resolves context and previews sample taxi rows. The pipeline declares two materialized views, with a dependency from the fares aggregate to the source trips.

See [Pipelines](pipelines.md) for the exact files and data flows.

## Configuration and testing

The Python package keeps YAML split by domain (`settings.yaml`, `ml.yaml`, `etl.yaml`). The loader validates these files with Pydantic, and the bundle sends catalog and schema to the wheel as explicit arguments. The standalone course notebooks take inputs from widgets and do not import the package configuration.

[Tests](../../tests/README.md) cover unit behavior, the entry-point chain without live Spark, and optional integration with Databricks Connect. [Tasks](../../tasks/README.md) and [fixtures](../../fixtures/README.md) are placeholders for future extensions.
