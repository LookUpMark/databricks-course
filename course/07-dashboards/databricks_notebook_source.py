# Databricks notebook source
# Assignment 07 - AI/BI Dashboards.
# Data-prep half of the assignment: builds the curated view a dashboard needs.
# The dashboard itself is created in the workspace UI (see README).

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 07 — Dashboards
# MAGIC
# MAGIC **Goal**: learn that dashboards are datasets + widgets, and datasets should
# MAGIC be curated views with business logic baked in — not raw tables.

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
# DBTITLE 1,Exercise 1 — curated view with revenue semantics
# COMMAND ----------
# Business logic lives in the view so every dashboard dataset agrees on it.
scratch = f"`{catalog}`.`{schema}`"

spark.sql(f"""
CREATE OR REPLACE VIEW {scratch}.v_orders_revenue AS
SELECT
  order_id,
  order_date,
  CASE WHEN status = 'paid' THEN amount ELSE 0 END AS revenue,
  status
FROM {scratch}.orders
""")
print("View created.")

# COMMAND ----------
# DBTITLE 1,Verify the datasets the dashboard will use
# COMMAND ----------
# Dataset 1: daily revenue trend
spark.sql(f"""
SELECT order_date, sum(revenue) AS daily_revenue
FROM {scratch}.v_orders_revenue GROUP BY order_date ORDER BY order_date
""").show()

# Dataset 2: revenue by status
spark.sql(f"""
SELECT status, sum(revenue) AS total FROM {scratch}.v_orders_revenue
GROUP BY status ORDER BY total DESC
""").show()

# Dataset 3: KPI
spark.sql(f"SELECT sum(revenue) AS total_revenue FROM {scratch}.v_orders_revenue").show()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 2-5 — build the dashboard in the UI
# MAGIC
# MAGIC 1. In the sidebar, select **New → Dashboard**.
# MAGIC 2. Select **Data → Add SQL dataset** for each query against
# MAGIC    `{catalog}.{schema}.v_orders_revenue`.
# MAGIC 3. Widgets: line chart (daily_revenue), bar chart (by status), counter (KPI).
# MAGIC 4. Choose the publication mode in LESSON.md, publish, and share with the intended viewers. With **Individual data permissions**, data access uses each viewer's permissions. Compute access uses the publisher's credentials.
# MAGIC
# MAGIC ## Deliverable
# MAGIC
# MAGIC Replace this cell with: published dashboard URL + one paragraph on which
# MAGIC widget you'd add for "ops health" and why.
