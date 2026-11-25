# Databricks notebook source
# Assignment 11 - Lakebase (managed Postgres OLTP).
# Creates only a synthetic Unity Catalog source table. List projects with the
# documented CLI and create a synced table only if the workspace authorizes it.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 11 — Lakebase
# MAGIC
# MAGIC **Goal**: see where Lakebase sits in the stack and prepare its data path.
# MAGIC
# MAGIC Lakebase = fully managed Postgres for apps/agents; Unity Catalog = our
# MAGIC lakehouse. The bridge between them: **synced tables** (UC → Postgres, managed read-only)
# MAGIC and registered databases may expose Postgres data to Unity Catalog where
# MAGIC that feature is available. Confirm behavior in your workspace UI.
# MAGIC
# COMMAND ----------
dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()

import re

_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not _IDENTIFIER.fullmatch(catalog) or not _IDENTIFIER.fullmatch(schema):
    raise ValueError("Set catalog and schema widgets to simple Unity Catalog identifiers before running write cells.")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Lesson recap
# MAGIC
# MAGIC | Concept | What it is |
# MAGIC |---|---|
# MAGIC | Project | Container for a Postgres database (created via UI / `databricks postgres create-project`) |
# MAGIC | Branch | Isolated copy — `production` by default; feature branches for dev work |
# MAGIC | Synced table | Unity Catalog table copied into Postgres (`_synced` suffix, read-only) |
# MAGIC | Registered catalog | Lakebase database visible as a read-only catalog in Unity Catalog |
# MAGIC
# MAGIC CLI: `databricks postgres list-projects` · UI: App switcher → Lakebase → Autoscaling
# MAGIC
# COMMAND ----------
# DBTITLE 1,Exercise 1 — list Lakebase projects from your terminal
# COMMAND ----------
# MAGIC %md
# MAGIC In an authenticated terminal, run `databricks postgres list-projects`. The list may be
# MAGIC empty or unavailable if the feature or permissions are not enabled. Record the project
# MAGIC and branch shown by your workspace; do not paste credentials here.


# COMMAND ----------
# DBTITLE 1,Exercise 2 — create the UC table a synced table would copy
# COMMAND ----------
# A synced table copies a UC table (main.default.x) into Postgres as
# <schema>.<table>_synced. This cell creates the source table.
src = f"`{catalog}`.`{schema}`"
spark.sql(f"""
CREATE OR REPLACE TABLE {src}.lakebase_source AS
SELECT * FROM VALUES
  (1, 'power_user', 0.92, DATE'2026-11-20'),
  (2, 'casual',     0.35, DATE'2026-11-21'),
  (3, 'power_user', 0.88, DATE'2026-11-22')
AS t(user_id, segment, engagement_score, last_seen_date)
""")
spark.sql(f"COMMENT ON TABLE {src}.lakebase_source IS 'SYNTHETIC DEMO DATA. Example UC source for an optional Lakebase snapshot exercise.'")
print(f"Created {src}.lakebase_source")

# COMMAND ----------
# DBTITLE 1,Inspect the source table (what the synced copy would reflect)
# COMMAND ----------
spark.sql(f"DESCRIBE TABLE {src}.lakebase_source").show(truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC In the workspace UI:
# MAGIC
# MAGIC 1. Catalog → `lakebase_source` → **Create** → **Synced table** (Snapshot mode).
# MAGIC    Confirm a read-only `<schema>.lakebase_source_synced` appears in the Lakebase SQL
# MAGIC    Editor, queryable with Postgres SQL.
# MAGIC 2. (Optional) Register the database in Unity Catalog and browse the new read-only catalog.
# MAGIC
# MAGIC Replace this cell's text with a summary: project name, branch, synced table name.
# MAGIC Then one paragraph: which tables would become synced snapshots (read-only, app-facing)
# MAGIC vs. which would stay in Postgres as the operational source of truth?
