# Assignment 07 — AI/BI Dashboards

## Before you start
Run the notebook cells to create the curated revenue view and inspect its datasets. Confirm the view exists in the scratch schema before creating dashboard widgets.

## Walkthrough
1. In the workspace navigation, open **Dashboards** and choose **Create** → **AI/BI Dashboard**. Name it for the assignment.
2. Add a dataset for each query shown in the notebook: daily revenue, revenue by status, and total revenue KPI. Use the fully qualified curated view as the source. Run each query in the dataset editor and confirm it returns rows.
3. Add a line chart bound to daily revenue, a bar chart bound to revenue by status, and a counter bound to the KPI dataset. Set the date/status and measure fields according to the query column names.
4. Arrange and title the widgets so the dashboard can be read without opening the queries. Save the dashboard.
5. Publish it using the dashboard's **Publish** action. Copy the published URL.
6. Configure viewer access in the share/permissions dialog. Grant access only to the intended viewers or group; verify they also have permission to query the underlying data/schema.
7. Add the URL to the notebook deliverable and explain one additional widget useful for operations health.

## Check your work
The dashboard is published, all three widgets render data from the curated view, and the intended viewers are listed in permissions.

## Deliverable
Record the published dashboard URL and one paragraph proposing an operations-health widget and why it helps.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
The notebook identity needs `USE CATALOG`, `USE SCHEMA`, and `CREATE TABLE`-equivalent view creation rights in the selected pre-created schema; viewers need catalog/schema usage and `SELECT` on the view. In **Workspace → Dashboards → Create → AI/BI dashboard**, add datasets from `<catalog>.<schema>.v_orders_revenue`, run each query, and confirm rows before adding a daily-revenue line chart, status bar chart, and total-revenue counter. Save, select **Publish**, and copy the actual URL; configure sharing for the intended group and verify its data grants. Delete only the dashboard you created; drop the view only if you own it and no other exercise depends on it.
