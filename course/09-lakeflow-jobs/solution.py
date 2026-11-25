# Databricks notebook source
# Assignment 09 - Lakeflow Jobs.
# This companion illustrates the job context. The bundle job itself uses src/sample_notebook.py.

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
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not catalog or not schema:
    raise ValueError("Set catalog and schema widgets to your pre-created writable Unity Catalog schema.")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("catalog and schema must be simple Unity Catalog identifiers (letters, digits, underscores).")

# COMMAND ----------
# DBTITLE 1,Exercise 1 — prove you are running inside a job

try:
    ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    job_group_id = ctx.jobGroupId().getOrElse(None)
    run_id = ctx.jobRunId().getOrElse(None)
    print(f"Job group id: {job_group_id}")
    print(f"Job run id:   {run_id}")
    if job_group_id is None:
        print("Interactive run: attach this notebook as a task to see real ids.")
except Exception as e:  # noqa: BLE001 - job context is unavailable outside Databricks
    print(f"Context unavailable: {e}")

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
# MAGIC Observe: job-level parameters (`catalog`, `schema`), the task retry
# MAGIC policy, and the dev-prefixed job name. Production is a separate deployment
# MAGIC mode with a stable root path and active schedule; describe that difference
# MAGIC in LESSON.md. The course bundle declares only the dev target.
# MAGIC
# MAGIC ## Deliverable
# MAGIC
# MAGIC Add a markdown cell with: deployed job URL, successful run ID, the DAG
# MAGIC design paragraph (ingest → train → evaluate: task types, dependencies,
# MAGIC retries), and what the dev configuration changes compared with a hypothetical production deployment.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Worked deliverable (example)
# MAGIC
# MAGIC Job link: `https://<workspace>/jobs/<job-id>` and run link: `https://<workspace>/jobs/<job-id>/runs/<run-id>` are synthetic URL shapes. Replace both with links from your dev deployment/run. The DAG in this bundle is notebook → (`python_wheel_task` and `refresh_pipeline` in parallel). A separate ingest → train → evaluate design could use a notebook ingest task, Python wheel training task, and notebook evaluation task with explicit dependencies and limited retries for transient failures.
# MAGIC
# MAGIC `--target dev` enables development mode, prefixes resource names, and pauses schedules. In a production bundle I would configure a stable root path, approved identity and an explicit schedule. This lab uses the personal `dev` target. Cleanup: undeploy only your dev bundle after saving evidence; never remove shared workspace resources.
