# Databricks notebook source
# Assignment 02 — Unity Catalog.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 02 — Unity Catalog
# MAGIC
# MAGIC Enter your assigned catalog and personal scratch schema. Empty defaults
# MAGIC intentionally prevent accidental writes to a shared/default schema.

# COMMAND ----------
import re

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not catalog or not schema:
    raise ValueError("Set both catalog and personal scratch schema widgets before writing.")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("Catalog and schema must be simple SQL identifiers (letters, digits, underscores).")

# COMMAND ----------
fq_schema = f"`{catalog}`.`{schema}`"
spark.sql(f"USE {fq_schema}")
print(f"Using schema: {spark.sql('SELECT current_schema()').first()[0]}")

# COMMAND ----------
# DBTITLE 1,Create a managed table with synthetic rows
table = f"{fq_schema}.`sample_features`"
data = [(i, round(i / 100, 4), f"synthetic_row_{i}") for i in range(100)]
spark.createDataFrame(data, ["id", "value", "label"]).write.mode("overwrite").saveAsTable(table)
spark.sql(f"DESCRIBE EXTENDED {table}").show(50, truncate=False)

# COMMAND ----------
# DBTITLE 1,Inspect grants when permitted
from pyspark.errors import AnalysisException

try:
    spark.sql(f"SHOW GRANTS ON SCHEMA {fq_schema}").show(truncate=False)
except AnalysisException:
    print("Could not inspect grants. Check the schema Permissions tab or ask its owner.")

# COMMAND ----------

# DBTITLE 1,Create and use a governed Volume
volume = f"{fq_schema}.`playbook_files`"
spark.sql(f"CREATE VOLUME IF NOT EXISTS {volume}")
volume_path = f"/Volumes/{catalog}/{schema}/playbook_files"
dbutils.fs.put(f"{volume_path}/hello.txt", "Hello from a UC Volume", overwrite=True)
print(dbutils.fs.head(f"{volume_path}/hello.txt"))
print(f"Table: {catalog}.{schema}.sample_features")
print(f"Volume: {catalog}.{schema}.playbook_files")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC Record the fully qualified managed table and volume paths. Explain when
# MAGIC you would use managed storage for scratch data. Keep the volume through topic 10.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Optional cleanup
# MAGIC
# MAGIC Run only after saving evidence. This drops only this assignment's named
# MAGIC table and volume, not the personal schema. Volume drop may require owner
# MAGIC privileges.

# COMMAND ----------
# Uncomment when cleanup is authorized:
# spark.sql(f"DROP TABLE IF EXISTS {table}")
# spark.sql(f"DROP VOLUME IF EXISTS {volume}")
