# Databricks notebook source
# Worked solution for Assignment 13. All rows are synthetic examples.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 13 — Worked solution
# MAGIC
# MAGIC The notebook's `orders` table is synthetic and stays in your personal schema. Its
# MAGIC comment provides a proposed definition for inspection; it does not prove it is modeled
# MAGIC Genie Ontology context or that a response used it, and is not a reason to certify the table.
# MAGIC Genie One and Genie Code search the same ontology, which combines governed modeled knowledge
# MAGIC with learned snippets from assets and usage. Context surfaced can vary by surface, feature,
# MAGIC permissions, and workspace configuration.

# COMMAND ----------
dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
# COMMAND ----------

catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()

import re

identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("Set catalog and your personal Assignment 02 schema widgets to simple identifiers.")

# COMMAND ----------
# DBTITLE 1,Inspect the topic 03 table and its comments
src = f"`{catalog}`.`{schema}`"
spark.sql(f"SHOW TABLES IN {src}").show(truncate=False)
spark.sql(f"SHOW VIEWS IN {src}").show(truncate=False)
spark.sql(f"DESCRIBE TABLE EXTENDED {src}.orders").show(80, truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Example observation template
# MAGIC
# MAGIC ```text
# MAGIC Genie One: record the actual answer and any SQL/citations the UI shows.
# MAGIC Genie Code: separately record any generated query or explanation, after reviewing it.
# MAGIC Conflict: hypothetical example — one generated query includes pending orders in revenue.
# MAGIC Do not claim a real conflict unless you observed it.
# MAGIC Certification: do not certify this synthetic personal-schema table.
# MAGIC Genie Code: inspect separately as an authoring assistant; do not conflate it with Genie One.
# MAGIC ```
