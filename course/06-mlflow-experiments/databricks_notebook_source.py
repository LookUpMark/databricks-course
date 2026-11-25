# Databricks notebook source
# Assignment 06 - MLflow Experiments.
# Trains 3 tiny scikit-learn models with autologging, finds the best run with
# search_runs, and logs an artifact. Optional: register to Unity Catalog.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 06 — MLflow Experiments
# MAGIC
# MAGIC **Goal**: structure experiments properly, compare runs programmatically.

# COMMAND ----------
# COMMAND ----------
# DBTITLE 1,Exercise 1 — experiment setup
# COMMAND ----------
from uuid import uuid4

import mlflow

current_user = spark.sql("SELECT current_user() AS user").first()["user"]
EXPERIMENT_PATH = f"/Users/{current_user}/databricks-course-experiments"
experiment = mlflow.set_experiment(EXPERIMENT_PATH)
session_id = uuid4().hex
print(f"Experiment: {EXPERIMENT_PATH}")

# COMMAND ----------
# DBTITLE 1,Exercise 2 — three training runs
# COMMAND ----------
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

mlflow.sklearn.autolog()

X, y = make_classification(n_samples=500, n_features=10, random_state=42)

for regularization in [0.1, 1.0, 10.0]:
    with mlflow.start_run(run_name=f"logreg-c{regularization:g}") as run:
        mlflow.set_tag("assignment", "06-mlflow")
        mlflow.set_tag("course_session", session_id)
        model = LogisticRegression(C=regularization, max_iter=200)
        auc = cross_val_score(model, X, y, cv=5, scoring="roc_auc").mean()
        model.fit(X, y)
        mlflow.log_metric("cv_auc", auc)

# COMMAND ----------
# DBTITLE 1,Exercise 3 — artifact in the best run
# COMMAND ----------
best = mlflow.search_runs(
    experiment_ids=[experiment.experiment_id],
    filter_string=f"tags.course_session = '{session_id}'",
    order_by=["metrics.cv_auc DESC", "attributes.start_time ASC"],
    max_results=1,
).iloc[0]
print(f"Best run: {best.run_id} (cv_auc={best['metrics.cv_auc']:.4f})")

with mlflow.start_run(run_id=best.run_id):
    mlflow.log_text(f"Best cv_auc: {best['metrics.cv_auc']}", "evaluation_report.txt")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 5 (optional) — register to Unity Catalog
# MAGIC
# MAGIC ```python
# MAGIC model_uri = f"runs:/{best.run_id}/model"
# MAGIC mlflow.register_model(model_uri, "YOUR_CATALOG.YOUR_SCHEMA.playbook_classifier")
# MAGIC # then set alias 'champion' on the new version
# MAGIC ```
# MAGIC Aliases (`@champion`) decouple consumers from version numbers — prefer them
# MAGIC for anything deployed.
