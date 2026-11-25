# Databricks notebook source
# Assignment 03 — Genie. All rows are synthetic.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 03 — Genie
# MAGIC
# MAGIC Enter your assigned catalog and personal scratch schema. Genie Agent setup
# MAGIC is a UI exercise; the notebook creates the synthetic data source only.

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
# MAGIC ## Deliverable
# MAGIC
# MAGIC Follow LESSON.md to create a Genie Agent, add two instructions and a trusted query,
# MAGIC and review the SQL behind three questions. Record the agent name, questions,
# MAGIC SQL review, and one instruction you refined. Keep the agent through topic 04
# MAGIC and the table through topics 05, 07 and 13.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Optional cleanup
# MAGIC
# MAGIC After saving evidence, drop only the assignment table if authorized:

# COMMAND ----------
# spark.sql(f"DROP TABLE IF EXISTS {orders}")
