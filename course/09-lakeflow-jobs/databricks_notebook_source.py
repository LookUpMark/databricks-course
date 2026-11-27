# Databricks notebook source
# Assignment 09 - Lakeflow Jobs.
# Companion lesson notebook; the real bundle job runs src/sample_notebook.py.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 09 — Lakeflow Jobs
# MAGIC
# MAGIC **Goal**: experience running as a job task and understand orchestration.
# MAGIC
# MAGIC You can run this interactively too, but the deliverable is a **job run**:
# MAGIC `databricks bundle deploy --target dev` then
# MAGIC `databricks bundle run sample_job --target dev`.

# COMMAND ----------
import re

dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
# COMMAND ----------

catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not catalog or not schema:
    raise ValueError("Set catalog and schema widgets to your pre-created writable Unity Catalog schema.")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("catalog and schema must be simple Unity Catalog identifiers (letters, digits, underscores).")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Companion and deployed sample
# MAGIC
# MAGIC This companion notebook is for reading the lesson and recording the exercise.
# MAGIC The bundle's real `sample_job` runs `src/sample_notebook.py`; that notebook
# MAGIC prints `job_run_id` and `task_run_id` widgets passed as `{{job.run_id}}` and
# MAGIC `{{task.run_id}}`. Inspect its task output for the actual IDs. This companion
# MAGIC does not infer IDs through the notebook JVM context.

# COMMAND ----------
# DBTITLE 1,Exercise 2 — task work: quick aggregate
import random

data = [(i, random.randint(0, 100)) for i in range(1000)]
df = spark.createDataFrame(data, ["id", "value"])
df.agg({"value": "avg"}).show()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 3-4 — deploy & run the bundle job (from your terminal)
# MAGIC
# MAGIC ```bash
# MAGIC export DATABRICKS_CONFIG_PROFILE=course
# MAGIC export BUNDLE_VAR_catalog='your_writable_catalog'
# MAGIC export BUNDLE_VAR_schema='course_yourname'
# MAGIC databricks bundle validate --target dev
# MAGIC databricks bundle deploy --target dev
# MAGIC databricks bundle run sample_job --target dev
# MAGIC ```
# MAGIC Observe: job-level parameters (`catalog`, `schema`), the job/task run IDs in
# MAGIC the deployed sample notebook output, and the dev-prefixed job name. The YAML
# MAGIC has no explicit retry policy. Choose one for your design exercise. Development mode prefixes
# MAGIC resource names and pauses the periodic trigger. A production target would explicitly configure
# MAGIC its deployment path, identity, and trigger state.
# MAGIC
# MAGIC Keep the deployed `catalog` and `schema` values for the run. A run override affects the notebook
# MAGIC and wheel. The pipeline uses the catalog and schema from deployment. Change the bundle variables
# MAGIC and redeploy `dev` to change the destination for the whole DAG.
# MAGIC
# MAGIC ## Deliverable
# MAGIC
# MAGIC Add a markdown cell with: deployed job URL, successful run ID and the job/task
# MAGIC run IDs from the deployed sample notebook task output, the DAG
# MAGIC design paragraph (ingest → train → evaluate: task types, dependencies,
# MAGIC chosen retry policy), and what the dev configuration changes compared with a hypothetical production deployment.
