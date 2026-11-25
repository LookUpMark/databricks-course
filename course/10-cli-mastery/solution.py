# Databricks notebook source
# Worked solution for Assignment 10. Run terminal commands on your host shell.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 10 — Worked solution
# MAGIC
# MAGIC This sample uses the course development bundle only. From the repository root:
# MAGIC
# MAGIC ```bash
# MAGIC export DATABRICKS_CONFIG_PROFILE=course
# MAGIC export BUNDLE_VAR_catalog='your_writable_catalog'
# MAGIC export BUNDLE_VAR_schema='course_yourname'
# MAGIC databricks bundle validate --target dev
# MAGIC databricks bundle run sample_job --target dev
# MAGIC ```
# MAGIC
# MAGIC The resource key is `sample_job`; in DAB development mode its display name is
# MAGIC `[dev <workspace-user-short-name>] sample_job`. Replace the placeholder with the
# MAGIC exact identity short name shown by your deployment. Volume
# MAGIC example: `dbfs:/Volumes/<catalog>/<schema>/playbook_files`. Auth diagnostics can
# MAGIC contain sensitive data: `databricks auth describe --profile course` should be inspected
# MAGIC locally, and only host/profile/auth type should be copied into course notes.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Runnable shell deliverable
# MAGIC
# MAGIC Save as `latest-job-state.sh`, pass the exact displayed job name as the first argument, and run
# MAGIC from an authenticated terminal with `jq` installed. It handles array and object responses,
# MAGIC zero or multiple exact matches, an empty run list, and missing state fields. It selects the run with the most recent start time.
# MAGIC
# MAGIC ```bash
# MAGIC #!/usr/bin/env bash
# MAGIC set -euo pipefail
# MAGIC if [[ $# -ne 1 ]]; then
# MAGIC   printf 'Usage: %s "exact job display name"\n' "$0" >&2
# MAGIC   exit 1
# MAGIC fi
# MAGIC job_name=$1
# MAGIC matches=$(databricks jobs list -o json | jq --arg name "$job_name" '
# MAGIC   (if type == "array" then . else .jobs // [] end)
# MAGIC   | map(select(.settings.name == $name))')
# MAGIC if [[ $(jq length <<< "$matches") -ne 1 ]]; then
# MAGIC   printf 'Expected one job named "%s", found %s\n' "$job_name" "$(jq length <<< "$matches")" >&2
# MAGIC   exit 1
# MAGIC fi
# MAGIC job_id=$(jq -er '.[0].job_id' <<< "$matches")
# MAGIC databricks jobs list-runs --job-id "$job_id" -o json | jq -er --arg name "$job_name" --arg id "$job_id" '
# MAGIC   (if type == "array" then . else .runs // [] end)
# MAGIC   | if length == 0 then error("no runs found") else max_by(.start_time // 0) end
# MAGIC   | "job=\($name) id=\($id) state=\(.state.result_state // .state.life_cycle_state // "unknown") start=\(.start_time // "unknown")"
# MAGIC '
# MAGIC ```
# MAGIC
# MAGIC Example output shape (illustrative, not a live result):
# MAGIC `job=[dev learner] sample_job id=123456 state=SUCCESS start=1730000000000`.
# MAGIC For CI/CD, `databricks bundle validate --target dev` is a useful pre-deploy check because
# MAGIC it validates bundle configuration before any deployment changes are made.
