# Assignment 14 — Databricks Apps

Worked example: [solution notebook](solution.py).

## Before you start
Run the notebook's read-only app inventory using the Databricks SDK's configured notebook authentication, or use the workspace UI fallback. The exercise is observational; do not deploy, start, stop, or delete apps.

## Walkthrough
1. Inspect the app list. Record names and lifecycle states; a URL may be omitted or unavailable. An empty list is a valid observation and may also reflect permissions.
2. Use the app switcher to open **Databricks Apps**. Open an app's **Overview** page and record its URL and displayed status, if present.
3. Inspect **Authorization** for the app identity/service principal. Use **Share** only to inspect the existing access list and `CAN USE`/`CAN MANAGE` entries; do not add, remove, or change sharing. This observation is limited to your permissions and does not prove universal access.
4. The sample `apps:` YAML in the solution is illustrative only. It does not assert an app exists or is deployed. If working from the course repo, `databricks bundle summary --target dev` is read-only; do not deploy for this assignment.
5. Add a Markdown cell with actual observed URL(s), state, and permission notes, or explicitly state no app was visible. Select which pattern best fits a hypothetical project: operations on Lakebase, an Agent Bricks agent, or analytics over Unity Catalog.

## Check your work
The SDK or UI inventory is recorded, and absence/inaccessibility is clearly documented. No deployment or permission change is needed.

## Deliverable
Record app URL(s) and who can use them, then explain which app pattern best fits this project and why.
