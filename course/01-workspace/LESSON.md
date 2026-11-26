# Assignment 01 — Workspace & Notebooks

## Before you start
Open the [assignment notebook](databricks_notebook_source.py) in your Databricks workspace and attach compute you have permission to use. Run its cells in order; it creates no Unity Catalog objects. Listing workspace assets from Python depends on support for Workspace Files and the selected environment. To list notebooks as workspace files, use Databricks Runtime 16.2 or newer, or serverless environment 2 or newer. If listing is unavailable, use the Workspace browser and record the limitation. See [Workspace Files limitations](https://docs.databricks.com/aws/en/files/workspace#limitations).

## Walkthrough
1. In the workspace browser, open **Workspace** and locate this notebook under your user folder. Right-click the notebook and choose **Copy > Path**; record that full workspace path.
2. Select available compute in the notebook compute selector and wait until it is attached. Run **Exercise 1 — inspect the runtime**. Record the compute type and its version separately: Databricks Runtime for classic compute, or the serverless environment version for serverless compute. Also record the Spark and Python versions printed by the notebook as separate values.
3. Workspace files hold notebooks and ordinary files; they are not DBFS. For governed data files use a Unity Catalog Volume (`/Volumes/<catalog>/<schema>/<volume>/...`) with the required `USE CATALOG`, `USE SCHEMA`, and volume privileges. `%fs` and `dbutils.fs` are interfaces, not equivalent storage systems. If your user folder cannot be listed from Python, use Workspace UI: click **Workspace** in the left sidebar, open **Users**, then your user folder. To get a notebook path, right-click it in the Workspace browser and choose **Copy > Path**.
4. Run **Exercise 3 — widgets**. It creates a text widget named `name` with the default `Learner`; enter a different value in the widget panel and rerun the greeting cell. Change the value again and rerun to confirm the input is read at execution time. The [sample job YAML](../../resources/sample_job.job.yml) shows how Jobs passes parameters to its notebook task.
5. Read the `%run` and `dbutils.notebook.run` explanation. `%run` includes another notebook in the current context; `dbutils.notebook.run` starts a nested execution and returns its exit value. Write one sentence about when you would use each.
6. Run the notebook-path cell and compare its result with the workspace breadcrumb. If they differ, record the value reported by the notebook and note the discrepancy.
7. Complete the deliverable cell at the bottom using the path and version values from your own run. Copy the workspace path with **Copy > Path** and use the Spark/Python versions printed by the notebook; do not copy the `<...>` example placeholders from the worked solution literally. Keep all outputs visible.

## Check your work
You should have a workspace path, separate compute environment, Spark and Python versions, a greeting using your widget value, and a written distinction between `%run` and nested notebook execution. If listing from Python is unavailable, right-click the notebook in the Workspace browser and choose **Copy > Path**. Record the error or feature limitation shown by your environment.

## Deliverable
Record the full notebook path, compute type/version, Spark version, Python version, and one difference between interactive attachment and job execution. Keep the executed notebook outputs.

## Cleanup
This assignment creates no persistent workspace objects. Detach compute when you finish if you do not need it.

## Worked solution

Compare your work with the [solution notebook](solution.py).
