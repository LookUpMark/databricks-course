# Assignment 07 — AI/BI Dashboards

## Before you start
Complete [topic 03](../03-genie/LESSON.md) and keep its `orders` table. Use the same catalog and existing personal schema in the notebook widgets. You need `USE CATALOG`, `USE SCHEMA`, `CREATE TABLE` on that schema to create the view, and `SELECT` on `orders`. You also need the Databricks SQL entitlement, `CAN USE` on a SQL warehouse, and permission to create and publish a dashboard. Create the view and verify the queries before starting the dashboard.

## Walkthrough
1. In the sidebar, select **New → Dashboard**. Name it for the assignment.
2. Under **Data**, select **Add SQL dataset** for each query shown in the notebook: daily revenue, revenue by status, and total revenue KPI. Use the fully qualified curated view as the source. Run each query in the dataset editor and confirm it returns rows.
3. Add a line chart bound to daily revenue, a bar chart bound to revenue by status, and a counter bound to the KPI dataset. Set the date/status and measure fields according to the query column names.
4. Arrange and title the widgets so the dashboard can be read without opening the queries. Save the dashboard.
5. Select **Publish** and choose a [data permission mode](https://docs.databricks.com/aws/en/dashboards/share/share).
   - **Share data permissions** uses the publisher's data and compute permissions. Use it only if you intend to share those results with the selected audience.
   - **Individual data permissions** evaluates data access using each viewer's own permissions. The warehouse uses the publisher's credentials. Grant viewers access to the dashboard and the Unity Catalog objects it queries.
6. Copy the published URL and share the dashboard with the intended users or group.
7. Add the URL to the notebook deliverable and explain one additional widget useful for operations health.

## Check your work
The dashboard is published, all three widgets render data from the curated view, and the intended viewers are listed in permissions.

## Deliverable
Record the published dashboard URL and one paragraph proposing an operations-health widget and why it helps.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Cleanup

Delete or unpublish the dashboard you created. Drop the revenue view only if you own it and no one needs it. Keep the topic 03 `orders` table through topic 13.
