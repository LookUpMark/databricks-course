# Assignment 11 — Lakebase

Worked example: [solution notebook](solution.py).

## Before you start
Run the project-list and source-table cells in the notebook. Use the personal schema created in Assignment 02. Lakebase project creation or synced-table setup may require workspace permissions; do not create a billable resource unless your workspace assignment authorizes it. This notebook creates only a clearly synthetic Unity Catalog source table; it does not provision Lakebase.

## Walkthrough
1. In a terminal, run `databricks postgres list-projects` using the course profile. Note an existing project and branch if your permissions allow listing. If this command is unavailable, record that limitation; do not use undocumented REST paths.
2. Run the UC source-table cell and inspect the table. This is the source whose data the synced table will copy.
3. In the workspace app launcher, open **Lakebase** (or **Postgres** if that is the displayed product name). Select the assigned project/database and its branch. Record the project and branch shown; do not create a project for this exercise.
4. In **Catalog Explorer**, navigate to the source table and choose **Create** → **Synced table** if available. Review the displayed mode, target project/branch and schema before confirming. Create a snapshot only if the workspace assignment explicitly permits it. If the action or permission is unavailable, record that limitation.
5. Open the Lakebase SQL Editor and inspect the synced table. Confirm its `_synced` suffix and query a few rows; treat it as read-only.
6. Optionally register the Lakebase database in Unity Catalog only if the workspace supports it and you have authorization. Confirm the resulting catalog is read-only.
7. Record project, branch, synced table, and which real-system tables should be synced snapshots versus operational Postgres sources of truth.

## Check your work
The synthetic source UC table is present. If an authorized snapshot was created, it appears in the selected Lakebase branch and is queryable there; otherwise record why the UI operation was unavailable.

## Deliverable
Record project name, branch, synced-table name (or why creation was unavailable), and one paragraph distinguishing synced read-only snapshots from Postgres source-of-truth tables.
