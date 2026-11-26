# Assignment 11 — Lakebase

Worked example: [solution notebook](solution.py).

## Before you start
Open the [assignment notebook](databricks_notebook_source.py), use the personal schema from [topic 02](../02-unity-catalog/LESSON.md), and set its `catalog` and `schema` widgets. List Lakebase projects in your terminal before selecting a project in the UI. Then run the notebook's Unity Catalog source-table cell; it creates and verifies the synthetic fixture. If a same-named table has a different schema or data, use a personal lab schema without that table. Create a sync only when the workspace assignment explicitly authorizes it.

## Walkthrough
1. In a terminal, run `databricks postgres list-projects` using the course profile. Copy an actual project ID from that output into `databricks postgres list-branches projects/<PROJECT_ID>`, replacing `<PROJECT_ID>` and removing the brackets. Run the branch command only for a project that was listed. Note an existing project and branch if your permissions allow listing. If either command is unavailable, record that limitation; do not use undocumented REST paths.
2. Run the UC source-table cell and inspect `lakebase_source`. Confirm its three synthetic rows and columns (`user_id`, `segment`, `engagement_score`, `last_seen_date`). This is the source whose data the synced table would copy.
3. In the workspace app launcher, open **Lakebase** (or **Postgres** if that is the displayed product name). Select the assigned project/database and its branch. Record the project and branch shown; do not create a project for this exercise.
4. In **Catalog Explorer**, navigate to the source table and choose **Create** → **Synced table** if available. Select the destination catalog and schema and enter a configurable destination table name. Choose Lakebase Postgres **Autoscaling**, then select project, branch and database. For a snapshot, choose **On-demand** and expand **Advanced settings** to select **Snapshot** (Snapshot and Triggered are both On-demand modes). Review all settings before confirming. The initial load starts on creation; subsequent Snapshot syncs are manual or scheduled. Create only if the workspace assignment explicitly permits it. If the action or permission is unavailable, record that limitation.
5. If you created the sync, open the Lakebase SQL Editor and inspect the synced table using the destination name you selected. Run `SELECT * FROM <destination_schema>.<destination_table> LIMIT 10;`, replacing both placeholders with the actual schema and table shown for your sync and omitting the angle brackets. This is a read-only check; treat the synced copy as read-only.
6. Optionally register the Lakebase database in Unity Catalog only if authorized: in Catalog Explorer choose **Create a catalog**, select **Lakebase Postgres** and **Autoscaling**, then select project, branch and database. This requires metastore `CREATE CATALOG`; querying/browsing the resulting read-only catalog requires serverless SQL warehouse or serverless notebook/job compute. Pro and classic compute are unsupported. If unavailable, record that limitation.
7. Record the observed project and branch, the exact destination table name you selected or why you skipped the sync, and which real-system tables should be synced snapshots or operational Postgres sources of truth. Keep project IDs, table names, and permission failures as observed; do not invent a project or URL.

## Check your work
The synthetic source UC table is present. If an authorized snapshot was created, it appears in the selected Lakebase branch and is queryable there; otherwise record why you skipped the sync.

## Deliverable
Record project name, branch, synced-table name (or why the sync was skipped), and one paragraph distinguishing synced read-only snapshots from Postgres source-of-truth tables.

## Cleanup

The notebook creates only the synthetic Unity Catalog source table. Do not delete a Lakebase project or branch for this assignment. If you created a synced table with authorization, remove only that assignment sync after saving evidence and confirming no one depends on it; drop the source table only when the dependent labs are complete.
