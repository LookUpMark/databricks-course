# Assignment 14 — Databricks Apps

Worked example: [solution notebook](solution.py).

## Before you start
Open the [assignment notebook](databricks_notebook_source.py) and run its read-only app inventory using the Databricks SDK's configured notebook authentication. If notebook authentication or the SDK call is unavailable, use the workspace UI fallback below and record the limitation. The exercise is observational; do not deploy, start, stop, or delete apps.

## Walkthrough
1. Inspect the notebook output. For each visible app, record `name`, `compute_state`, `app_state`, and `url`; either state or URL may be absent. An empty list is a valid observation and may also reflect permissions, so do not treat it as proof that no app exists.
2. In the workspace app switcher, open **Databricks Apps**. Compare the UI list with the notebook inventory. Open an app's **Overview** page and record its URL and displayed status, if present.
3. Inspect **Authorization** for the app identity/service principal. Use **Share** only to inspect the existing access list and `CAN USE`/`CAN MANAGE` entries; do not add, remove, or change sharing. This observation is limited to your permissions and does not prove universal access.
4. The sample `apps:` YAML in the solution is illustrative only. It does not assert an app exists or is deployed. If working from the course repo, `databricks bundle summary --target dev` is read-only; do not deploy for this assignment.
5. Add a Markdown cell with observed app URLs, states, and permission notes, or state that no app was visible. Explain which pattern best fits the project. Consider an analytics dashboard over Unity Catalog, an operational app backed by Lakebase, or an agent interface powered by Agent Bricks.

## Check your work
The SDK or UI inventory records each visible app's name, compute state, app state, and URL where available. Any empty result, missing field, or access limitation is clearly documented. No deployment or permission change is needed.

## Deliverable
Record app URL(s) and who can use them, then explain which app pattern best fits this project and why.

## Cleanup

This is a read-only inspection exercise and creates no workspace resources to clean up.
