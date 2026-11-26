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
# MAGIC | Compute | Managed serverless app compute; inspect `compute_status.state` and `app_status.state` |
# MAGIC | Access | **Overview** shows app details; **Authorization** shows app identity; **Share** shows user/group access |
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
from databricks.sdk import WorkspaceClient

client = WorkspaceClient()
apps = list(client.apps.list())
print(f"{len(apps)} app(s) visible to this identity")
for app in apps:
    compute_status = getattr(app, "compute_status", None)
    app_status = getattr(app, "app_status", None)
    print(
        {
            "name": getattr(app, "name", None),
            "compute_state": getattr(compute_status, "state", None),
            "app_state": getattr(app_status, "state", None),
            "url": getattr(app, "url", None),
        }
    )


# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC In the app switcher, open **Databricks Apps**. Open each app's **Overview** page for
# MAGIC status/URL, **Authorization** for the app identity, and **Share** to inspect existing
# MAGIC `CAN USE`/`CAN MANAGE` permissions. Do not change sharing.
# MAGIC Then a markdown cell:
# MAGIC
# MAGIC 1. The URL(s) you found + who can use them.
# MAGIC 2. In one paragraph, choose a pattern for the project and explain why. Consider an
# MAGIC    analytics dashboard over curated Unity Catalog data, an operational app backed by
# MAGIC    Lakebase, or an agent interface powered by Agent Bricks.
