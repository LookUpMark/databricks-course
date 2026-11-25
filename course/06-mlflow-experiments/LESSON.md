# Assignment 06 — MLflow Experiments

## Before you start
Attach compute with MLflow and scikit-learn available. Use a workspace experiment path under your user folder unless the notebook provides an assigned path.

## Walkthrough
1. Run the setup cell to set the experiment. Confirm the experiment path printed by MLflow.
2. Run the training cell to create three runs with different hyperparameters. In the Databricks workspace, open **Machine Learning → Experiments** (or use the experiment link printed in the notebook) and confirm all three runs appear.
3. Run the artifact cell to log the text report to the selected best run. Open that run in the UI and inspect its **Artifacts** section.
4. Run the search cell. Confirm it selects the best run using the intended metric and that the result corresponds to one of the three visible runs.
5. Optionally register the model in Unity Catalog if you have the required privileges. If not, leave it at the logged-artifact stage and record that registration was skipped.
6. Add a Markdown cell with experiment path, best run ID, metric value, and when you would use an alias instead of a fixed model version.

## Check your work
The UI shows three runs and the report artifact; `search_runs` identifies the best run by the chosen metric.

## Deliverable
Keep the executed notebook and record the experiment path, best run ID and metric, and one sentence comparing aliases with fixed versions.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use notebook compute with MLflow and scikit-learn. The notebook creates its experiment beneath the signed-in user's workspace folder, so you need permission to create experiments there. In **Machine Learning → Experiments**, open the printed experiment and verify three runs; open the selected run's **Artifacts** and inspect `evaluation_report.txt`. UC model registration is optional and requires model creation/registration privileges. Remove only your experiment when its evidence is no longer needed.
