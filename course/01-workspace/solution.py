# Databricks notebook source
# Worked solution for Assignment 01. UI paths and runtime values below are examples.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 01 — worked solution
# MAGIC
# MAGIC This example demonstrates the expected evidence. Replace every illustrative
# MAGIC workspace path and runtime value with values from your own workspace.
# MAGIC
# MAGIC **Example deliverable (illustrative only):**
# MAGIC - Workspace path: `/Workspace/Users/<your-email>/course/01-workspace/solution`
# MAGIC - Compute type/version: Serverless, environment 5 (illustrative); for classic compute, record its Databricks Runtime version.
# MAGIC - Spark: `<version printed below>`
# MAGIC - Python: `<version printed below>`
# MAGIC - Interactive notebooks stay attached to the selected compute; a job task
# MAGIC   starts under the job's configured compute and receives task parameters.

# COMMAND ----------
import sys

print(f"Spark version: {spark.version}")
print(f"Python version: {sys.version.split()[0]}")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Workspace and storage
# MAGIC
# MAGIC Workspace folders store notebooks and ordinary workspace files. A Unity
# MAGIC Catalog Volume stores governed data files. A path listing can fail when
# MAGIC the caller lacks access. In that case click **Workspace** in the sidebar,
# MAGIC open **Users** and your folder, then open the notebook and choose
# MAGIC right-click the notebook in Workspace and choose **Copy > Path**.

# COMMAND ----------
from pathlib import Path

username = spark.sql("SELECT current_user()").first()[0]
try:
    print([item.name for item in sorted((Path("/Workspace/Users") / username).iterdir())[:10]])
except OSError:
    print("Workspace files unavailable from Python. Open the Workspace UI instead.")

# COMMAND ----------
dbutils.widgets.text("name", "Learner")
name = dbutils.widgets.get("name").strip()
if not name:
    raise ValueError("Set the name widget to a non-empty value.")
print(f"Hello, {name}!")

# COMMAND ----------
# MAGIC %md
# MAGIC **Example observation:** `%run` shares definitions in the current notebook
# MAGIC context. `dbutils.notebook.run` starts a separate nested run and returns an
# MAGIC exit string. Use the former for shared setup and the latter for an isolated
# MAGIC notebook execution with parameters.

# COMMAND ----------

# DBTITLE 1,Read the notebook path
try:
    context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    print(f"Notebook path: {context.notebookPath().get()}")
except Exception:  # noqa: BLE001 - access to notebook context varies by compute
    print("Right-click the notebook in Workspace and choose **Copy > Path**.")
