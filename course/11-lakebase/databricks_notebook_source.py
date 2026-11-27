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
# COMMAND ----------

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
# MAGIC | Synced table | Unity Catalog table copied into Postgres (destination name is selected during creation) |
# MAGIC | Registered catalog | Lakebase database visible as a read-only catalog in Unity Catalog |
# MAGIC
# MAGIC CLI: `databricks postgres list-projects`, then `databricks postgres list-branches projects/<PROJECT_ID>` · UI: app switcher → Lakebase Postgres → Autoscaling
# MAGIC
# COMMAND ----------
# DBTITLE 1,Exercise 1 — list Lakebase projects from your terminal
# MAGIC %md
# MAGIC In an authenticated terminal, run `databricks postgres list-projects`, then
# MAGIC `databricks postgres list-branches projects/<PROJECT_ID>` for an observed project ID.
# MAGIC Results may be empty or unavailable if the feature or permissions are not enabled.
# MAGIC Record the project and branch actually shown; do not paste credentials here.


# COMMAND ----------
# DBTITLE 1,Exercise 2 — create the UC table a synced table would copy
# A synced table copies a UC table (main.default.x) into Postgres under the
# destination table name selected in the create-synced-table flow.
source_table = f"`{catalog}`.`{schema}`.lakebase_source"
fixture = """
SELECT * FROM VALUES
  (1, 'power_user', 0.92, DATE '2026-11-20'),
  (2, 'casual',     0.35, DATE '2026-11-21'),
  (3, 'power_user', 0.88, DATE '2026-11-22')
AS t(user_id, segment, engagement_score, last_seen_date)
"""
spark.sql(f"""
CREATE TABLE IF NOT EXISTS {source_table}
USING DELTA
COMMENT 'SYNTHETIC DEMO DATA. Example UC source for a Lakebase snapshot.'
AS {fixture}
""")

expected = spark.sql(fixture)
source = spark.table(source_table)
expected_rows = expected.orderBy("user_id").collect()
if (
    source.schema.simpleString() != expected.schema.simpleString()
    or source.orderBy("user_id").take(len(expected_rows) + 1) != expected_rows
):
    raise ValueError(
        f"{source_table} already contains different data or has a different schema. "
        "Use a personal lab schema without that table before creating a sync."
    )
print(f"Verified synthetic source table: {source_table}")

# COMMAND ----------
# DBTITLE 1,Inspect the source table (what the synced copy would reflect)
spark.sql(f"DESCRIBE TABLE {source_table}").show(truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC In the workspace UI:
# MAGIC
# MAGIC 1. Catalog → `lakebase_source` → **Create** → **Synced table**. Choose the destination
# MAGIC    catalog/schema and enter the destination table name. Select Lakebase Postgres
# MAGIC    **Autoscaling**, project, branch and database. For a snapshot, choose **On-demand**,
# MAGIC    then **Advanced settings** → **Snapshot**. Snapshot and Triggered are both On-demand
# MAGIC    modes. The initial load starts at creation; later Snapshot syncs are manual or scheduled.
# MAGIC    Review all settings and create only when authorized. The table name is configurable.
# MAGIC 2. (Optional, permission-dependent) Catalog Explorer → **Create a catalog** → **Lakebase
# MAGIC    Postgres** → **Autoscaling**; select project, branch and database. This requires
# MAGIC    metastore `CREATE CATALOG`. Browse/query the read-only registered catalog with serverless
# MAGIC    SQL warehouse or serverless notebook/job compute; Pro/classic compute is unsupported.
# MAGIC
# MAGIC Record the project name, branch, and synced table name, or explain why you skipped the sync.
# MAGIC Then one paragraph: which tables would become synced snapshots (read-only, app-facing)
# MAGIC vs. which would stay in Postgres as the operational source of truth?
