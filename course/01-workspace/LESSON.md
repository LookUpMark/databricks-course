# Assignment 01 — Workspace & Notebooks

## Before you start
Open the assigned notebook in the Databricks workspace and attach it to available compute. You need permission to view the notebook and use the selected compute; workspace or compute permissions are granted by your administrator. Keep the notebook open to inspect outputs.

## Walkthrough
1. In the workspace browser, open **Workspace** and locate this notebook under your user folder. Right-click the notebook and choose **Copy > Path**; record that full workspace path.
2. Select available compute in the notebook compute selector and wait until it is attached. Record the compute type and its version separately: Databricks Runtime for classic compute, or the serverless environment version for serverless compute. Also record the Spark and Python versions printed by the notebook as separate values.
3. Workspace files hold notebooks and ordinary files; they are not DBFS. For governed data files use a Unity Catalog Volume (`/Volumes/<catalog>/<schema>/<volume>/...`) with the required `USE CATALOG`, `USE SCHEMA`, and volume privileges. `%fs` and `dbutils.fs` are interfaces, not equivalent storage systems. If your user folder cannot be listed from Python, use Workspace UI: click **Workspace** in the left sidebar, open **Users**, then your user folder. To get a notebook path, right-click it in the Workspace browser and choose **Copy > Path**.
4. Create the `name` widget from the widget cell or widget panel, enter a value, and run the greeting cell. Change the value and rerun to confirm the input is read at execution time.
5. Read the `%run` and `dbutils.notebook.run` explanation. `%run` includes another notebook in the current context; `dbutils.notebook.run` starts a nested execution and returns its exit value. Write one sentence about when you would use each.
6. Run the notebook-path cell and compare its result with the workspace breadcrumb. If they differ, record the value reported by the notebook and note the discrepancy.
7. Complete the deliverable cell at the bottom and keep all outputs visible.

## Check your work
You should have a workspace path, separate compute environment, Spark and Python versions, a greeting using your widget value, and a written distinction between `%run` and nested notebook execution. A workspace listing may be denied by design; right-click the notebook in the Workspace browser and choose **Copy > Path**; report the permission limitation.

## Deliverable
Record the full notebook path, compute type/version, Spark version, Python version, and one difference between interactive attachment and job execution. Keep the executed notebook outputs.

## Cleanup
This assignment creates no persistent workspace objects. Detach compute when you finish if you do not need it.

## Worked solution

Compare your work with the [solution notebook](solution.py).
