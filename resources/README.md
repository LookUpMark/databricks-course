# Bundle resources

Both YAML files are loaded by [databricks.yml](../databricks.yml) and used in the [Lakeflow Jobs lab](../course/09-lakeflow-jobs/LESSON.md).

- [sample_job.job.yml](sample_job.job.yml) defines the job parameters, the notebook task, and the two parallel downstream tasks. The wheel task installs the built `playbook` package. The pipeline task points to the deployed pipeline by resource key. The development target pauses the periodic trigger.
- [playbook_etl.pipeline.yml](playbook_etl.pipeline.yml) declares the serverless Lakeflow pipeline, the destination catalog and schema, and the Python transformations to execute.

From the project root, follow [Run the bundle](../README.md#run-the-bundle) to set the profile and variables, then run `databricks bundle validate --target dev` before deployment. Add future resources as separate YAML files here so the main configuration remains small.
