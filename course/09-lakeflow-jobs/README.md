# Assignment 09 — Lakeflow Jobs

Deploy and inspect a development job run and its task graph.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- The deployed job name/URL and successful run ID, plus the job and task run IDs printed in the sample notebook task output, in a markdown cell.
- The DAG design paragraph (notebook, wheel, and pipeline tasks in the deployed sample job).
- What development mode changed in the deployed resource names and trigger state.

## Access, expected result, and cleanup
Use the `course` CLI profile and the privileges in the [lesson](LESSON.md#before-you-start). Validate and deploy `dev` from the repository root, then run `sample_job` with its deployed defaults. Open the run URL, or find `[dev <workspace-user-short-name>] sample_job` in **Jobs & Pipelines**. The notebook task prints its job and task run IDs. Inspect the two parallel downstream tasks in the run graph, then save the evidence before [cleaning up](../../README.md#run-the-bundle).
