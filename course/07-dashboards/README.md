# Assignment 07 — AI/BI Dashboards

Build and publish a dashboard from curated datasets.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- Executed notebook creating the curated view.
- Published dashboard URL in a markdown cell.
- One markdown paragraph: which widget you'd add for "ops health" and why.

## Access, expected result, and cleanup
The notebook identity needs `USE CATALOG`, `USE SCHEMA`, and `CREATE TABLE`-equivalent view creation rights in the selected pre-created schema; viewers need catalog/schema usage and `SELECT` on the view. In **Workspace → Dashboards → Create → AI/BI dashboard**, add datasets from `<catalog>.<schema>.v_orders_revenue`, run each query, and confirm rows before adding a daily-revenue line chart, status bar chart, and total-revenue counter. Save, select **Publish**, and copy the actual URL; configure sharing for the intended group and verify its data grants. Delete only the dashboard you created; drop the view only if you own it and no other exercise depends on it.
