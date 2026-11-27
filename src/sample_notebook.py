# Databricks notebook source
# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.

# COMMAND ----------
# MAGIC %md
# MAGIC # Bundle job setup
# MAGIC
# MAGIC The job in `resources/sample_job.job.yml` passes its catalog and schema
# MAGIC parameters and its job/task run IDs to this notebook as widgets.
# MAGIC The pipeline task uses the catalog and schema configured at deployment.

# COMMAND ----------

# DBTITLE 1,Check job parameters and schema
import re
import sys

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
dbutils.widgets.text("job_run_id", "")
dbutils.widgets.text("task_run_id", "")
# COMMAND ----------

catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
job_run_id = dbutils.widgets.get("job_run_id").strip()
task_run_id = dbutils.widgets.get("task_run_id").strip()
if not all(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part) for part in (catalog, schema)):
    raise ValueError("Set catalog and schema to simple Unity Catalog identifiers before running the job.")

spark.sql(f"USE `{catalog}`.`{schema}`")
print(f"Target: {catalog}.{schema}")
print(f"Job run ID:  {job_run_id or '(not supplied; run from the bundle job)'}")
print(f"Task run ID: {task_run_id or '(not supplied; run from the bundle job)'}")
print(f"Spark: {spark.version}; Python: {sys.version.split()[0]}")

# COMMAND ----------

# DBTITLE 1,Preview a Spark DataFrame
display(spark.range(5).withColumnRenamed("id", "value"))
