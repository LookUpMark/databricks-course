# Databricks notebook source
# Assignment 13 - Genie Ontology (context layer for AI agents).
# Inventories synthetic UC data and inspects metadata that can inform Genie One.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 13 — Genie Ontology
# MAGIC
# MAGIC **Goal**: inspect data metadata and context that can inform Genie One.
# MAGIC
# MAGIC The synthetic data and comments below are examples only; they do not establish that
# MAGIC Genie will use them or that the table is certified or production quality.
# MAGIC
# COMMAND ----------
dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()

import re

_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not _IDENTIFIER.fullmatch(catalog) or not _IDENTIFIER.fullmatch(schema):
    raise ValueError(
        "Set catalog and schema widgets to simple Unity Catalog identifiers before inspecting topic 03 data."
    )

# COMMAND ----------
# MAGIC %md
# MAGIC ## Lesson recap
# MAGIC
# MAGIC | Layer | Source | Authority |
# MAGIC |---|---|---|
# MAGIC | **Genie One** | Simplified interface for business users to interact with data assets | Inspect documented UI behavior |
# MAGIC | **Genie Code** | Coding and data assistant for technical practitioners | Inspect generated code before running |
# MAGIC
# MAGIC Observe Genie One responses and Genie Code separately. Do not infer that they expose
# MAGIC the same context or that every workspace has the same UI features.
# MAGIC
# COMMAND ----------
# DBTITLE 1,Inspect the topic 03 table and its comments
src = f"`{catalog}`.`{schema}`"
spark.sql(f"SHOW TABLES IN {src}").show(truncate=False)
spark.sql(f"SHOW VIEWS IN {src}").show(truncate=False)
spark.sql(f"DESCRIBE TABLE EXTENDED {src}.orders").show(80, truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC In the UI:
# MAGIC
# MAGIC 1. Catalog → your personal schema (from the widgets) → inspect `orders`; do not certify synthetic data.
# MAGIC 2. Review the data access and visible context controls; record any limitation.
# MAGIC 3. Ask Genie One a question (e.g. "monthly revenue") and inspect any available SQL or citations.
# MAGIC 4. Optionally inspect Genie Code separately as an authoring assistant. Do not conflate it with Genie One.
# MAGIC
# MAGIC Replace this cell's text with a summary: modeled assets, learned-only assets, one
# MAGIC real or clearly hypothetical discrepancy, and why synthetic scratch data must not be certified.
