# Assignment 09 — Lakeflow Jobs

Deploy and inspect a development job run and its task graph.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- The deployed job name/URL and the successful run ID in a markdown cell.
- The DAG design paragraph (notebook, wheel, and pipeline tasks in the deployed sample job).
- What development mode changed in the deployed resource names and trigger state.

## Access, expected result, and cleanup
Run commands from the bundle repository root with an authenticated CLI profile named `course`; the identity needs permission to validate/deploy the bundle, create/run jobs, use serverless job environments, and create/refresh the Unity Catalog pipeline and its destination tables. Set `BUNDLE_VAR_catalog` and `BUNDLE_VAR_schema` to an existing writable destination. Validate first, deploy only `dev`, then run `sample_job`. The expected DAG is `notebook_task` followed by `python_wheel_task` and `refresh_pipeline` in parallel; inspect the run graph and task logs in **Jobs & Pipelines → Jobs → sample_job → Runs**. Development mode prefixes resource names and pauses the periodic trigger. Production mode uses a stable root path and enables schedules, so it requires a deliberate release and permissions; do not deploy prod in this assignment. When finished, remove only your development bundle resources after saving the job/run evidence.
