# Databricks notebook source
# Worked solution for Assignment 14. This is an observer exercise only.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 14 — Worked solution
# MAGIC
# MAGIC Use the notebook's authenticated Databricks SDK client to list apps read-only. If SDK
# MAGIC support is unavailable in the current runtime, use the app switcher → **Databricks Apps** and
# MAGIC record the visible results. An empty list can mean none are visible to this identity.
# MAGIC The app configuration below is illustrative; this assignment does not deploy an app.

# COMMAND ----------
# DBTITLE 1,Read-only workspace app inventory
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
# MAGIC ## Sample app resource configuration (illustrative only)
# MAGIC
# MAGIC ```yaml
# MAGIC resources:
# MAGIC   apps:
# MAGIC     example_app:
# MAGIC       name: example-app
# MAGIC       source_code_path: ../src/example_app
# MAGIC ```
# MAGIC
# MAGIC This snippet is a configuration example, not a deployed app or evidence that the source
# MAGIC directory exists. Databricks Apps run in managed serverless compute; access and data
# MAGIC authorization depend on app permissions and its configured identity/credentials. Review
# MAGIC the actual app details and permission panel rather than assuming Unity Catalog access is
# MAGIC inherited. Record the app URL only when the workspace actually displays one.

# COMMAND ----------
# MAGIC %md
# MAGIC In the UI, use **Overview** for URL/status, **Authorization** for app identity, and
# MAGIC **Share** to inspect existing `CAN USE`/`CAN MANAGE` access. Do not change permissions.
# MAGIC
# MAGIC ## Example report (fill from live observation)
# MAGIC
# MAGIC ```text
# MAGIC Apps visible: none observed in this example; replace with your actual result.
# MAGIC URL/state/permissions: not observed; do not infer deployment from the YAML snippet.
# MAGIC Fit: an analytics app is a reasonable candidate for read-only views over curated UC data;
# MAGIC an operational app may fit Lakebase; an agent interface may fit Agent Bricks. Select based
# MAGIC on actual project requirements and explicitly grant only required data access.
# MAGIC ```
