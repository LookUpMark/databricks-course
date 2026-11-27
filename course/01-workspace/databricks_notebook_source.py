# Databricks notebook source
# Assignment 01 - Workspace & Notebooks.
# Lesson + exercise + deliverable for the Databricks ML Engineer playbook.
# Run on supported Databricks notebook compute. Use the Workspace UI if file listing is unavailable.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 01 — Workspace & Notebooks
# MAGIC
# MAGIC **Goal**: get comfortable with the Databricks Workspace, notebook source
# MAGIC format, widgets and dbutils.
# MAGIC
# MAGIC Read the lesson cells, run the exercise cells, and complete the deliverable
# MAGIC at the bottom.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Lesson — what you need to know
# MAGIC
# MAGIC - You can open notebooks from workspace folders, including your user folder and Git folders.
# MAGIC - This file is a **`.py` Databricks notebook source**: the first line
# MAGIC   `# Databricks notebook source` marks the format, `# COMMAND ----------`
# MAGIC   separates cells, `# MAGIC %md` marks markdown.
# MAGIC - `dbutils` is the notebook toolbox: widgets (parameters), fs (files),
# MAGIC   secrets (credentials), notebook (workflow helpers).
# MAGIC - Widgets let the same notebook run interactively **and** as a job task
# MAGIC   with parameters (see `resources/sample_job.job.yml`).

# COMMAND ----------
# DBTITLE 1,Exercise 1 — inspect the runtime
import sys

print(f"Spark version: {spark.version}")
print(f"Python: {sys.version.split()[0]}")

# COMMAND ----------
# DBTITLE 1,Exercise 2 — explore Workspace files
from pathlib import Path

username = spark.sql("SELECT current_user()").first()[0]
try:
    print([item.name for item in sorted((Path("/Workspace/Users") / username).iterdir())[:10]])
except OSError:
    print("Workspace files unavailable from Python. Open the Workspace UI instead.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise 3 — widgets
# MAGIC
# MAGIC Create a widget `name`, read it and print a greeting. Change the widget
# MAGIC value from the widget panel at the top of the notebook and re-run.

# COMMAND ----------
dbutils.widgets.text("name", defaultValue="Learner")
# COMMAND ----------

name = dbutils.widgets.get("name")
print(f"Hello, {name}! Widgets are the standard way to parameterize notebooks.")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 4 — `%run` and `dbutils.notebook`
# MAGIC
# MAGIC `%run <path>` inlines another notebook (shared setup, functions).
# MAGIC `dbutils.notebook.run("<path>", timeout)` launches it as a *nested job run*
# MAGIC and returns its exit value. In a sentence below, state when you would pick
# MAGIC one over the other.
# MAGIC
# MAGIC **Your answer**: (write here)

# COMMAND ----------
# DBTITLE 1,Exercise 5 — find this notebook's own path
# In a job run the path is available through the task context.
try:
    ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    print(f"Notebook path: {ctx.notebookPath().get()}")
except Exception:  # noqa: BLE001 - notebook context varies by compute
    print("In Workspace, right-click the notebook and choose Copy > Path.")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC Add a markdown cell below (use `# MAGIC %md`) with:
# MAGIC
# MAGIC 1. This notebook's full workspace path.
# MAGIC 2. The compute type and its version (Databricks Runtime for classic compute, environment version for serverless). Record Spark and Python versions separately.
# MAGIC 3. One difference between interactive attach and job execution.
