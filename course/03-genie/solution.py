# Databricks notebook source
# Worked solution for Assignment 03. All rows are synthetic examples.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 03 — worked solution
# MAGIC
# MAGIC Enter your assigned catalog and personal scratch schema. Genie Agent setup
# MAGIC is a UI exercise; the notebook creates the synthetic data source only.

# COMMAND ----------
import re

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
# COMMAND ----------

catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not catalog or not schema:
    raise ValueError("Set both catalog and personal scratch schema widgets before writing.")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("Catalog and schema must be simple SQL identifiers.")
fq_schema = f"`{catalog}`.`{schema}`"

# COMMAND ----------
orders = f"{fq_schema}.`orders`"
spark.sql(f"""
CREATE OR REPLACE TABLE {orders} AS
SELECT * FROM VALUES
  (1, 100.0, 'paid', DATE'2026-01-10'),
  (2, 250.0, 'paid', DATE'2026-02-15'),
  (3, 80.0, 'refund', DATE'2026-03-01'),
  (4, 120.0, 'paid', DATE'2026-04-20'),
  (5, 300.0, 'pending', DATE'2026-05-11')
AS t(order_id, amount, status, order_date)
""")
spark.sql(f"COMMENT ON TABLE {orders} IS 'SYNTHETIC e-commerce orders. Revenue is sum(amount) where status is paid.'")
spark.sql(f"ALTER TABLE {orders} ALTER COLUMN order_id COMMENT 'Synthetic order identifier.'")
spark.sql(f"ALTER TABLE {orders} ALTER COLUMN amount COMMENT 'Synthetic order amount in EUR.'")
spark.sql(
    f"ALTER TABLE {orders} ALTER COLUMN status COMMENT 'Synthetic status: paid, pending, or refund. Only paid counts as revenue.'"
)
spark.sql(f"ALTER TABLE {orders} ALTER COLUMN order_date COMMENT 'Synthetic order date.'")
spark.sql(f"DESCRIBE TABLE {orders}").show(truncate=False)

# COMMAND ----------
# DBTITLE 1,Expected answer for monthly paid revenue
spark.sql(f"""
SELECT date_format(order_date, 'yyyy-MM') AS month, sum(amount) AS revenue_eur
FROM {orders}
WHERE status = 'paid'
GROUP BY date_format(order_date, 'yyyy-MM')
ORDER BY month
""").show()

# COMMAND ----------
# MAGIC %md
# MAGIC ## UI walkthrough and example review
# MAGIC
# MAGIC In the workspace sidebar, select **Genie Agents → New**, choose the `orders` table, and select **Create**.
# MAGIC Review any suggestions from Genie Code. Under **Configure**, add two instructions: count only paid orders
# MAGIC as revenue and report currency in EUR. Save the SQL above in **Examples**, ask three questions, and inspect each
# MAGIC generated SQL, and give feedback on the weakest response.
# MAGIC
# MAGIC **Synthetic example deliverable:** agent name `course-synthetic-orders`;
# MAGIC questions: “What is total paid revenue?”, “Show paid revenue by month”,
# MAGIC “How many orders are pending?”; expected totals are 470 EUR, 100/250/120 EUR
# MAGIC for Jan/Feb/Apr 2026, and 1 pending order. The SQL is correct only if it
# MAGIC applies the stated status filter. Example values are not workspace evidence.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Optional cleanup
# MAGIC
# MAGIC After saving evidence, drop only the assignment table if authorized:

# COMMAND ----------
# spark.sql(f"DROP TABLE IF EXISTS {orders}")
