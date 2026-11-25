# Assignment 09 — Lakeflow Jobs

## Before you start
Review `resources/sample_job.job.yml` and ensure the Databricks CLI is authenticated to the intended workspace. The exercise deploys to `dev`; do not deploy to production as part of this walkthrough.

## Walkthrough
1. In the YAML, identify the `notebook_task`, `python_wheel_task`, and `refresh_pipeline` task types, parameters, compute configuration, and dependencies. The sample job YAML has no explicit retry policy; note this separately from the retry policy you choose for your design exercise. Note the job key `sample_job`.
2. From the bundle repository root, select the named CLI profile and provide the catalog and your pre-created writable schema:
   ```bash
   export DATABRICKS_CONFIG_PROFILE=course
   export BUNDLE_VAR_catalog='your_writable_catalog'
   export BUNDLE_VAR_schema="your_writable_schema"
   databricks bundle validate --target dev
   ```
   Replace `your_writable_schema` with the real schema identifier; inspect validation errors before deployment.
3. Deploy and run only the dev target:
   ```bash
   databricks bundle deploy --target dev
   databricks bundle run sample_job --target dev
   ```
   Wait for the command to return a run URL or ID.
4. Open the run URL in the workspace UI. Inspect task status, dependency graph, compute, parameters, logs, and output. Confirm the run succeeded. In the `notebook_task` output, record the `Job run ID` and `Task run ID` printed by the sample notebook; these are passed using supported dynamic value references.
5. In the Jobs UI, open the deployed job and compare its `[dev ...]` name with the resource definition. Do not deploy `prod` for this exercise.
6. Design a separate three-task ingest → train → evaluate DAG in a Markdown cell. Specify task types, dependencies, and a sensible retry policy; also state what the `dev` target changed.

## How a production target would differ

This bundle deploys only the personal `dev` target. A separate production
configuration would use a managed identity, an owner-controlled deployment
path, and an explicit trigger schedule and permissions. The following fragment
illustrates the mode; a real production target requires those additional settings.

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
Run commands from the bundle repository root with an authenticated CLI profile named `course`; the identity needs permission to validate/deploy the bundle, create/run jobs, use serverless job environments, and create/refresh the Unity Catalog pipeline and its destination tables. Set `BUNDLE_VAR_catalog` and `BUNDLE_VAR_schema` to an existing writable destination. Validate first, deploy only `dev`, then run `sample_job`. The expected DAG is `notebook_task` followed by `python_wheel_task` and `refresh_pipeline` in parallel; inspect the run graph and task logs in **Jobs & Pipelines → Jobs → sample_job → Runs**. Development mode prefixes resource names and pauses the periodic trigger. The course has only a development target. When finished, remove only your development bundle resources after saving the job/run evidence.
