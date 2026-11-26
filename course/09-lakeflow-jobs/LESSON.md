# Assignment 09 — Lakeflow Jobs

## Before you start
Open the [companion notebook](databricks_notebook_source.py), follow the [bundle setup](../../README.md#run-the-bundle), and use an existing [personal Unity Catalog schema](../02-unity-catalog/LESSON.md). From the repository root, review the [job YAML](../../resources/sample_job.job.yml) and the [pipeline YAML](../../resources/playbook_etl.pipeline.yml). This walkthrough deploys and runs only the `dev` target.

The pipeline's run-as identity needs `USE CATALOG`, `USE SCHEMA`, and `CREATE MATERIALIZED VIEW` on the destination. It also needs `SELECT` on `samples.nyctaxi.trips` and usage privileges on the source catalog and schema. The job's identity needs usage privileges on the destination and read access to the same sample table for the wheel task. See [pipeline permissions](https://docs.databricks.com/aws/en/ldp/privileges) and [Unity Catalog requirements for pipelines](https://docs.databricks.com/aws/en/ldp/unity-catalog#requirements).

## Walkthrough
1. In the YAML, identify the `notebook_task`, `python_wheel_task`, and `refresh_pipeline` task types, parameters, compute configuration, and dependencies. The sample job YAML has no explicit retry policy; note this separately from the retry policy you choose for your design exercise. Note the job key `sample_job`.
2. From the bundle repository root, select the named CLI profile and provide the catalog and your pre-created writable schema:
   ```bash
   export DATABRICKS_CONFIG_PROFILE=course
   export BUNDLE_VAR_catalog='your_writable_catalog'
   export BUNDLE_VAR_schema="your_writable_schema"
   databricks bundle validate --target dev
   ```
   Replace both placeholders with the real catalog and schema identifiers. Use letters, digits, and underscores, starting with a letter or underscore. Inspect validation errors before deployment.
3. Continue only after `bundle validate` succeeds and its output has no unresolved errors. Deploy and run only the dev target:
   ```bash
   databricks bundle deploy --target dev
   databricks bundle run sample_job --target dev
   ```
   Wait for the command to return a run URL or ID.
4. Open the run URL in the workspace UI. Inspect task status, dependency graph, compute, parameters, logs, and output. Confirm the run succeeded. In the [notebook task](../../src/sample_notebook.py) output, record the `Job run ID` and `Task run ID` printed by the sample notebook; these are passed using supported dynamic value references.
5. In **Jobs & Pipelines**, find the deployed job whose name starts with `[dev` and ends with `sample_job`; the middle part is your workspace user short name, so do not search for the angle-bracket text literally. Compare the displayed name with the `sample_job` resource key.
6. Design a separate three-task ingest → train → evaluate DAG in a Markdown cell. Specify task types, dependencies, and a sensible retry policy; also state what the `dev` target changed.

### How catalog and schema reach the tasks

A job run override of `catalog` or `schema` changes the notebook widgets and wheel arguments. The pipeline task runs the existing pipeline, which publishes to the catalog and schema set when the bundle was deployed. For the lab, run with the deployed defaults. To move the whole DAG to another personal schema, update `BUNDLE_VAR_catalog` and `BUNDLE_VAR_schema`, then redeploy `dev` before running again. See [job parameter pushdown](https://docs.databricks.com/aws/en/jobs/job-parameters#job-parameter-pushdown) and [pipeline destinations](https://docs.databricks.com/aws/en/ldp/target-schema).

## How a production target would differ

This bundle defines the personal `dev` target. In `development` mode, the CLI prefixes deployed resource names and pauses the periodic trigger. For a production target, configure the deployment identity, an owner-controlled `workspace.root_path`, the desired trigger state, and permissions explicitly. The following fragment selects the mode. See [bundle deployment modes](https://docs.databricks.com/aws/en/dev-tools/bundles/deployment-modes).

```yaml
targets:
  prod:
    mode: production
```

## Check your work
The dev job exists and its run completed successfully; the UI run details match the task graph and parameters in the bundle, and the notebook task output shows its job and task run IDs.

## Deliverable
Record the dev job URL, successful run ID from the job run, job and task run IDs from the notebook task output, DAG design, and what the dev target changed in the deployed resource.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
The deploying identity needs permission to create and run jobs and pipelines on serverless compute in the selected workspace. The expected DAG is `notebook_task` followed by `python_wheel_task` and `refresh_pipeline` in parallel. Within the pipeline, the fares aggregate reads the trips materialized view. Save the job and run evidence before following the [bundle cleanup instructions](../../README.md#run-the-bundle).
