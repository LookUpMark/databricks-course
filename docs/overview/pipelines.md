# Job and pipeline walkthrough

## sample_job

The job is defined in [resources/sample_job.job.yml](../../resources/sample_job.job.yml) and used by [topics 09](../../course/09-lakeflow-jobs/LESSON.md) and [10](../../course/10-cli-mastery/LESSON.md). Its periodic trigger is paused when deployed in development mode.

| Task | Implementation | What happens |
|---|---|---|
| `notebook_task` | [src/sample_notebook.py](../../src/sample_notebook.py) | Reads the job parameters as widgets, selects the schema, and displays five sample rows. |
| `python_wheel_task` | [playbook.main](../../src/playbook/main.py) | Installs the wheel, calls `main` with the job parameters, and previews `samples.nyctaxi.trips`. |
| `refresh_pipeline` | [playbook_etl.pipeline.yml](../../resources/playbook_etl.pipeline.yml) | Runs the deployed pipeline in parallel with the wheel task once the notebook succeeds. |

See [Run the bundle](../../README.md#run-the-bundle) for the local commands, setup and cleanup.

## playbook_etl

The pipeline executes in serverless Lakeflow compute and publishes into the bundle's configured catalog and schema. Its batch queries use `@dp.materialized_view`.

1. [sample_trips_playbook.py](../../src/playbook_etl/transformations/sample_trips_playbook.py) reads the Databricks sample taxi trips.
2. [sample_zones_playbook.py](../../src/playbook_etl/transformations/sample_zones_playbook.py) reads the first view and aggregates its fares by pickup ZIP.

The [Medallion ETL lab](../../course/08-etl-pipelines/LESSON.md) teaches the separate bronze/silver/gold pattern with Delta tables in a notebook.

## Course notebooks

Labs run independently in the workspace using the prerequisites in the [course index](../../course/README.md) and their own lesson. To compare your output with a worked example, open the corresponding `solution.py` in Databricks.
