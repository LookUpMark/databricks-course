# Assignment 10 — Databricks CLI Mastery

Worked example: [solution notebook](solution.py).

## Before you start
Run these commands in a local Bash terminal, not in a notebook `%sh` cell, so the CLI uses your local authentication profile. Install the supported Databricks CLI and authenticate to the intended workspace. Select the course profile with `export DATABRICKS_CONFIG_PROFILE=course`; authenticate with `databricks auth login --host 'https://<workspace-url>' --profile course` if it is not configured. Never paste tokens or unmasked auth output into a notebook.

## Walkthrough
1. Run `databricks --version` and `databricks auth describe --profile course`. Confirm host and authentication type. Treat credentials as secrets: share only the profile name and host, and redact tokens, client secrets, and any credential values.
2. Use `databricks workspace list '/Workspace/Users/<your-email>'` and export a folder with `databricks workspace export-dir '<workspace-path>' '<local-path>'`. Confirm notebook source files are present.
3. Run `databricks jobs list -o json` and inspect the top-level JSON shape before selecting fields. Depending on CLI output, the jobs can be a list or under the top-level `jobs` property. Use `jq -r '(if type == "array" then . else .jobs // [] end)[] | .settings.name'`.
4. From the repository root, set `export DATABRICKS_CONFIG_PROFILE=course`, `export BUNDLE_VAR_catalog='your_writable_catalog'`, and `export BUNDLE_VAR_schema='course_yourname'`. Run `databricks bundle run sample_job --target dev` after completing the [Lakeflow Jobs deployment](../09-lakeflow-jobs/LESSON.md). In Jobs, use the exact generated display name `[dev <workspace-user-short-name>] sample_job` (the short name is specific to the authenticated identity). Confirm it with `databricks bundle summary --target dev` or the Jobs UI before running the script. Inspect runs with `databricks jobs list-runs --job-id '<id>' -o json`.
5. List the [topic 02 volume](../02-unity-catalog/LESSON.md) with `databricks fs ls 'dbfs:/Volumes/<catalog>/<schema>/playbook_files'` and confirm the expected sample file.
6. Complete the exact-name script in the notebook. It must reject missing and ambiguous matches and handle no runs. Use the current [Jobs API status fields](https://docs.databricks.com/api/jobs/v2/list-runs) and support the legacy state fields as a fallback. Report an unknown state if neither has a value.
7. Add a Markdown cell naming a CI/CD command and explaining why.

## Check your work
Workspace export and volume listing succeed, and the script prints the latest-started-run state summary or a clear missing/ambiguous result without exposing credentials. The current root bundle uses the profile and `BUNDLE_VAR_*` variables above; confirm values from the checked-in [bundle configuration](../../databricks.yml) before running a deploy.

## Deliverable
Save the shell script in an ignored local `deliverables/` directory, and add the CI/CD command explanation to the notebook.
