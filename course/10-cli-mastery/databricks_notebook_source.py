# Databricks notebook source
# Assignment 10 - CLI Mastery.
# Companion notebook: documents and exercises the CLI workflow that pairs with
# the terminal. The deliverable is a shell script (see README) - this notebook
# records the lesson and lets you paste/verify CLI results in-cell.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 10 — CLI Mastery
# MAGIC
# MAGIC **Goal**: drive Databricks entirely from the terminal.
# MAGIC
# MAGIC Run the commands in your shell; paste key outputs into the deliverable cell.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Lesson cheatsheet
# MAGIC
# MAGIC | Group | Typical use |
# MAGIC |---|---|
# MAGIC | `bundle validate/deploy/run/destroy` | IaC loop for this repo |
# MAGIC | `workspace list/export/export-dir` | notebooks in/out of the workspace |
# MAGIC | `jobs list / bundle run` | trigger and inspect runs |
# MAGIC | `fs ls` | DBFS and `/Volumes/...` paths |
# MAGIC | `pipelines list` | Lakeflow Spark Declarative Pipelines |
# MAGIC | `lakeview list` / `lakeview get` | AI/BI Dashboards |
# MAGIC | `auth describe` | debug authentication |
# MAGIC
# MAGIC Scripting tips: add `-o json`, inspect the JSON shape, check exit codes, and use
# MAGIC `DATABRICKS_CONFIG_PROFILE=course` for this course workspace. Never log token values.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 1-4 — run these locally (not `%sh`, keep auth on your host)
# MAGIC
# MAGIC ```bash
# MAGIC databricks --version
# MAGIC databricks auth describe --profile course
# MAGIC databricks workspace export-dir '/Workspace/Users/your-email/databricks-course' ./course-copy
# MAGIC databricks jobs list -o json | jq -r '(if type == "array" then . else .jobs // [] end)[] | .settings.name'
# MAGIC export DATABRICKS_CONFIG_PROFILE=course
# MAGIC export BUNDLE_VAR_catalog='your_writable_catalog'
# MAGIC export BUNDLE_VAR_schema='course_yourname'
# MAGIC databricks bundle run sample_job --target dev  # DAB dev display: [dev <workspace-user-short-name>] sample_job
# MAGIC databricks fs ls 'dbfs:/Volumes/your_writable_catalog/course_yourname/playbook_files'
# MAGIC ```

# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC Write `latest-job-state.sh`. The script should take the exact display name as
# MAGIC its argument, list jobs as JSON, find exactly one match, and display the state of its latest-started
# MAGIC run. Handle the missing and ambiguous cases plus a job with no runs.
# MAGIC
# MAGIC Start with:
# MAGIC
# MAGIC ```bash
# MAGIC #!/usr/bin/env bash
# MAGIC set -euo pipefail
# MAGIC job_name="$1"
# MAGIC databricks jobs list -o json
# MAGIC # Add exact-name selection and jobs list-runs here.
# MAGIC ```
# MAGIC
# MAGIC Explain which Databricks CLI command you would use in CI/CD and why.
