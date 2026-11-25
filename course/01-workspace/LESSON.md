# Assignment 01 — Workspace & Notebooks

## Before you start
Open the assigned notebook in the Databricks workspace and attach it to available compute. You need permission to view the notebook and use the selected compute; workspace or compute permissions are granted by your administrator. Keep the notebook open to inspect outputs.

## Walkthrough
1. In the workspace browser, open **Workspace** and locate this notebook under your user folder. Use the notebook menu or its breadcrumb to identify its full workspace path.
2. Select an available cluster in the compute selector and wait until it is attached. On classic compute, record the Databricks Runtime version shown in its details. On serverless, record Serverless and the environment version shown in the notebook UI. Record the Spark and Python versions printed by the notebook separately.
3. Workspace files hold notebooks and ordinary files; they are not DBFS. For governed data files use a Unity Catalog Volume (`/Volumes/<catalog>/<schema>/<volume>/...`) with the required `USE CATALOG`, `USE SCHEMA`, and volume privileges. `%fs` and `dbutils.fs` are interfaces, not equivalent storage systems. If your user folder cannot be listed from Python, use Workspace UI: click **Workspace** in the left sidebar, open **Users**, then your user folder. To get a notebook path, open it and use **File > Copy path** (or copy its breadcrumb path).
4. Create the `name` widget from the widget cell or widget panel, enter a value, and run the greeting cell. Change the value and rerun to confirm the input is read at execution time.
5. Read the `%run` and `dbutils.notebook.run` explanation. `%run` includes another notebook in the current context; `dbutils.notebook.run` starts a nested execution and returns its exit value. Write one sentence about when you would use each.
6. Run the notebook-path cell and compare its result with the workspace breadcrumb. If they differ, record the value reported by the notebook and note the discrepancy.
7. Complete the deliverable cell at the bottom and keep all outputs visible.

## Check your work
You should have a workspace path, separate compute environment, Spark and Python versions, a greeting using your widget value, and a written distinction between `%run` and nested notebook execution. A workspace listing may be denied by design; use the UI path-copy fallback and report the permission limitation.

## Deliverable
Record the full notebook path, runtime version, and one difference between interactive attachment and job execution. Keep the executed notebook outputs.

## Cleanup
This assignment creates no persistent workspace objects. Detach compute when you finish if you do not need it.

## Worked solution

Compare your work with the [solution notebook](solution.py).
