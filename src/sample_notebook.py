# Databricks notebook source
# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.

# MAGIC %md
# MAGIC # Bundle job setup
# MAGIC
# MAGIC The job in `resources/sample_job.job.yml` passes its catalog and schema
# MAGIC parameters to the notebook as widgets.

# COMMAND ----------

# DBTITLE 1,Check job parameters and schema
import re
import sys

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
if not all(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part) for part in (catalog, schema)):
    raise ValueError("Set catalog and schema to simple Unity Catalog identifiers before running the job.")

spark.sql(f"USE `{catalog}`.`{schema}`")
print(f"Target: {catalog}.{schema}")
print(f"Spark: {spark.version}; Python: {sys.version.split()[0]}")

# COMMAND ----------

# DBTITLE 1,Preview a Spark DataFrame
display(spark.range(5).withColumnRenamed("id", "value"))
