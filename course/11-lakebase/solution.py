# Databricks notebook source
# Worked solution for Assignment 11. Table rows are synthetic examples only.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 11 — Worked solution
# MAGIC
# MAGIC Example terminal observation: `databricks postgres list-projects`, then
# MAGIC `databricks postgres list-branches projects/<PROJECT_ID>`, may return a project
# MAGIC list, an empty list, or a permission/feature error. Record only what your workspace
# MAGIC actually shows. Never invent a project, branch, or synced table. Creating a Lakebase
# MAGIC resource or synced table is optional and requires explicit workspace authorization.

# COMMAND ----------
dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()

import re

identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("Set catalog and your personal Assignment 02 schema widgets to simple identifiers.")

# COMMAND ----------
# DBTITLE 1,Create a synthetic Unity Catalog source table
src = f"`{catalog}`.`{schema}`"
spark.sql(f"""
CREATE OR REPLACE TABLE {src}.lakebase_source AS
SELECT * FROM VALUES
  (1, 'synthetic_user_a', 0.92),
  (2, 'synthetic_user_b', 0.35),
  (3, 'synthetic_user_c', 0.88)
AS t(user_id, segment, engagement_score)
""")
spark.sql(
    f"COMMENT ON TABLE {src}.lakebase_source IS 'SYNTHETIC DEMO DATA. Example source for an optional Lakebase snapshot exercise.'"
)
spark.sql(f"SELECT * FROM {src}.lakebase_source ORDER BY user_id").show(truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Example deliverable
# MAGIC
# MAGIC ```text
# MAGIC Project/branch: not inspected in this example; fill from the assigned workspace.
# MAGIC Synced table: not created. Create only if explicitly authorized.
# MAGIC Data rule: a UC synced snapshot is an app-facing copy; operational Postgres records
# MAGIC remain in Postgres when Postgres is the system of record.
# MAGIC ```
# MAGIC
# MAGIC If authorized, Catalog Explorer → source table → **Create** → **Synced table**. Choose
# MAGIC destination catalog/schema and enter a destination table name; select Lakebase Postgres
# MAGIC Autoscaling, project, branch and database. Snapshot is under **On-demand** → **Advanced
# MAGIC settings**. The initial load begins at creation; later snapshots are manual or scheduled.
# MAGIC Review settings before confirming. In Lakebase SQL Editor, inspect
# MAGIC the actual destination and sample rows. Clean up only resources created for this exercise
# MAGIC and only when your workspace instructions permit it.
