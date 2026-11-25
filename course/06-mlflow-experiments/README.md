# Assignment 06 — MLflow Experiments

Compare tracked runs, inspect artifacts, and identify the best run.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- Executed notebook: 3 runs visible, best run found via `search_runs`.
- A markdown cell with the experiment path, best run id and its metric, and one
  sentence on when you would use aliases vs. fixed version numbers.

## Access, expected result, and cleanup
Use notebook compute with MLflow and scikit-learn. The notebook creates its experiment beneath the signed-in user's workspace folder, so you need permission to create experiments there. In **Machine Learning → Experiments**, open the printed experiment and verify three runs; open the selected run's **Artifacts** and inspect `evaluation_report.txt`. UC model registration is optional and requires model creation/registration privileges. Remove only your experiment when its evidence is no longer needed.
