# Databricks notebook source
# Assignment 14 - Databricks Apps (managed web apps in the workspace).
# Lists apps read-only through the authenticated Databricks SDK and documents
# an illustrative DAB resource snippet. This notebook deploys nothing.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 14 — Databricks Apps
# MAGIC
# MAGIC **Goal**: understand the serving layer of the stack and inspect live apps.
# MAGIC
# MAGIC Databricks Apps are managed app hosting in a workspace. Review the actual app details,
# MAGIC identity, permissions, and data access; do not assume access is inherited from Unity Catalog.
# MAGIC
# COMMAND ----------
# MAGIC %md
# MAGIC ## Lesson recap
# MAGIC
# MAGIC | Aspect | Detail |
# MAGIC |---|---|
# MAGIC | Configuration | A bundle may declare an `apps:` resource |
# MAGIC | Compute | Managed serverless app compute; inspect current app details for state |
# MAGIC | Access | Depends on app permissions and configured identity/credentials |
# MAGIC | Observation | Read app metadata and permissions; this notebook makes no changes |
# MAGIC
# COMMAND ----------
# MAGIC %md
# MAGIC ## The bundle resource (context — do NOT deploy in this exercise)
# MAGIC
# MAGIC ```yaml
# MAGIC resources:
# MAGIC   apps:
# MAGIC     example_app:
# MAGIC       name: example-app
# MAGIC       source_code_path: ../src/example_app
# MAGIC ```
# MAGIC
# MAGIC This YAML is illustrative only. It does not mean an app exists or is deployed.
# MAGIC
# COMMAND ----------
# DBTITLE 1,Exercise 1 — list apps via the REST API
# COMMAND ----------
from databricks.sdk import WorkspaceClient

client = WorkspaceClient()
apps = list(client.apps.list())
print(f"{len(apps)} app(s) visible to this identity")
for app in apps:
    print({"name": app.name, "state": getattr(app, "compute_status", None), "url": getattr(app, "url", None)})


# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC In the UI, open each app you found: check permissions and copy the URL if shown.
# MAGIC Then a markdown cell:
# MAGIC
# MAGIC 1. The URL(s) you found + who can use them.
# MAGIC 2. One paragraph: what this project's app would do — ops dashboard over curated UC
# MAGIC    tables, an agent from Assignment 12, or an app against Lakebase (Assignment 11)?
