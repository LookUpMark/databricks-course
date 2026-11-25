# Assignment 11 — Lakebase

Worked example: [solution notebook](solution.py).

## Before you start
Run the project-list and source-table cells in the notebook. Use the personal schema created in Assignment 02. Lakebase project creation or synced-table setup may require workspace permissions; do not create a billable resource unless your workspace assignment authorizes it. This notebook creates only a clearly synthetic Unity Catalog source table; it does not provision Lakebase.

## Walkthrough
1. In a terminal, run `databricks postgres list-projects` using the course profile. For an observed project ID, inspect branches with `databricks postgres list-branches projects/<PROJECT_ID>`. Note an existing project and branch if your permissions allow listing. If either command is unavailable, record that limitation; do not use undocumented REST paths.
2. Run the UC source-table cell and inspect the table. This is the source whose data the synced table will copy.
3. In the workspace app launcher, open **Lakebase** (or **Postgres** if that is the displayed product name). Select the assigned project/database and its branch. Record the project and branch shown; do not create a project for this exercise.
4. In **Catalog Explorer**, navigate to the source table and choose **Create** → **Synced table** if available. Select the destination catalog and schema and enter a configurable destination table name. Choose Lakebase Postgres **Autoscaling**, then select project, branch and database. For a snapshot, choose **On-demand** and expand **Advanced settings** to select **Snapshot** (Snapshot and Triggered are both On-demand modes). Review all settings before confirming. The initial load starts on creation; subsequent Snapshot syncs are manual or scheduled. Create only if the workspace assignment explicitly permits it. If the action or permission is unavailable, record that limitation.
5. Open the Lakebase SQL Editor and inspect the synced table using the destination name you selected. Query a few rows; treat it as read-only.
6. Optionally register the Lakebase database in Unity Catalog only if authorized: in Catalog Explorer choose **Create a catalog**, select **Lakebase Postgres** and **Autoscaling**, then select project, branch and database. This requires metastore `CREATE CATALOG`; querying/browsing the resulting read-only catalog requires serverless SQL warehouse or serverless notebook/job compute. Pro and classic compute are unsupported. If unavailable, record that limitation.
7. Record project, branch, synced table, and which real-system tables should be synced snapshots versus operational Postgres sources of truth.

## Check your work
The synthetic source UC table is present. If an authorized snapshot was created, it appears in the selected Lakebase branch and is queryable there; otherwise record why the UI operation was unavailable.

## Deliverable
Record project name, branch, synced-table name (or why creation was unavailable), and one paragraph distinguishing synced read-only snapshots from Postgres source-of-truth tables.
