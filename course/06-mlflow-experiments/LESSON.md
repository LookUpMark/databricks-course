# Assignment 06 — MLflow Experiments

## Before you start
Open the [assignment notebook](databricks_notebook_source.py) and attach compute with [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) and scikit-learn available. The notebook creates an experiment under your signed-in user's folder; use the path it prints rather than substituting a different experiment.

## Walkthrough
1. Run the setup cell to set the experiment. Confirm the experiment path printed by MLflow.
2. Run the training cell once to create three runs (`logreg-c0.1`, `logreg-c1`, and `logreg-c10`) with different regularization values. In the Databricks workspace, open **Machine Learning → Experiments**, find the printed experiment path, and confirm all three runs appear.
3. Run the search and report cell. It selects the run with the highest `cv_auc` from this notebook session (earliest start time breaks a tie) and adds `evaluation_report.txt` to that run. Confirm the printed run ID and metric, open the run, select **Artifacts**, and inspect the report.
4. The notebook explicitly logs each model with MLflow 3 and saves the returned model URI with its run. Optionally register the best run using that URI in Unity Catalog if you have privileges to create the registered model and model version. In the optional example, replace `YOUR_CATALOG` and `YOUR_SCHEMA` in `YOUR_CATALOG.YOUR_SCHEMA.playbook_classifier` with your actual Unity Catalog names before running it; the literal placeholder name will fail. If you lack the required privileges, leave the model at the logged-artifact stage and record that registration was skipped.
5. Add a Markdown cell with experiment path, best run ID, metric value, and when you would use an alias instead of a fixed model version.

## Check your work
The UI shows three runs and the report artifact; `search_runs` identifies the best run by the chosen metric.

## Deliverable
Keep the executed notebook and record the experiment path, best run ID and metric, and one sentence comparing aliases with fixed versions. If registered, the model owner can set an alias such as `champion` on the approved version with `USE CATALOG` and `USE SCHEMA`. See [alias permissions](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle#set-and-delete-aliases-on-models).

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use notebook compute with MLflow 3 and scikit-learn. The notebook creates its experiment beneath the signed-in user's workspace folder, so you need permission to create experiments there. In **Machine Learning → Experiments**, open the printed experiment and verify three runs; open the selected run's **Artifacts** and inspect `evaluation_report.txt`. UC model registration is optional and requires privileges to create/use the registered model and create a model version; use the best run's logged model URI. If you use the URI pattern `models:/<model_id>`, replace `<model_id>` with the actual model ID; do not paste the angle brackets literally. Creating a model version on an existing model requires ownership or `CREATE MODEL VERSION`, plus `USE CATALOG` and `USE SCHEMA`. Setting an alias requires ownership and the same usage privileges. Remove only your experiment when its evidence is no longer needed.
