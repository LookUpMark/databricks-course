# Assignment 07 — AI/BI Dashboards

## Before you start
Complete [topic 03](../03-genie/LESSON.md) and keep its `orders` table. Use the same catalog and existing personal schema in the notebook widgets. You need `USE CATALOG`, `USE SCHEMA`, `CREATE TABLE` on that schema to create the view, and `SELECT` on `orders`. You also need the Databricks SQL entitlement, `CAN USE` on a SQL warehouse, and permission to create and publish a dashboard.

In the [notebook](databricks_notebook_source.py), run the setup and **Exercise 1 — curated view** cells with your catalog and schema. This creates `<catalog>.<schema>.v_orders_revenue`. Then run the verification queries in the next cell to check that the view returns data. Do this preparation once before creating the dashboard; the `CREATE VIEW` statement is not a dashboard dataset query.

## Walkthrough
1. In the sidebar, select **New → Dashboard**. Name it for the assignment.
2. Under **Data**, select **Add SQL dataset** and create three separate datasets. Before running each query, replace `YOUR_CATALOG` and `YOUR_SCHEMA` with the exact catalog and schema you entered in the notebook widgets. Keep the backticks around the identifiers, but do not paste the placeholder names literally. The notebook's `CREATE VIEW` statement is already run in the preparation step above; add only these `SELECT` queries as datasets:

   **Daily revenue**

   ```sql
   SELECT order_date, SUM(revenue) AS daily_revenue
   FROM `YOUR_CATALOG`.`YOUR_SCHEMA`.v_orders_revenue
   GROUP BY order_date
   ORDER BY order_date
   ```

   **Revenue by status**

   ```sql
   SELECT status, SUM(revenue) AS total
   FROM `YOUR_CATALOG`.`YOUR_SCHEMA`.v_orders_revenue
   GROUP BY status
   ORDER BY total DESC
   ```

   **Total revenue KPI**

   ```sql
   SELECT SUM(revenue) AS total_revenue
   FROM `YOUR_CATALOG`.`YOUR_SCHEMA`.v_orders_revenue
   ```

   Run each query in the dataset editor and confirm it returns rows. If you paste `YOUR_CATALOG` or `YOUR_SCHEMA` unchanged, the query will fail: use the real widget values instead.
3. Add a line chart bound to **Daily revenue**, a bar chart bound to **Revenue by status**, and a counter bound to **Total revenue KPI**. Use the date/status and measure fields returned by those queries.
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
