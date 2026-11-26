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
# DBTITLE 1,Exercise 1 — experiment setup
from uuid import uuid4

import mlflow

current_user = spark.sql("SELECT current_user() AS user").first()["user"]
EXPERIMENT_PATH = f"/Users/{current_user}/databricks-course-experiments"
experiment = mlflow.set_experiment(EXPERIMENT_PATH)
session_id = uuid4().hex
print(f"Experiment: {EXPERIMENT_PATH}")

# COMMAND ----------
# DBTITLE 1,Exercise 2 — three training runs
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

mlflow.sklearn.autolog(log_models=False)

X, y = make_classification(n_samples=500, n_features=10, random_state=42)

for regularization in [0.1, 1.0, 10.0]:
    with mlflow.start_run(run_name=f"logreg-c{regularization:g}") as run:
        mlflow.set_tag("assignment", "06-mlflow")
        mlflow.set_tag("course_session", session_id)
        model = LogisticRegression(C=regularization, max_iter=200)
        auc = cross_val_score(model, X, y, cv=5, scoring="roc_auc").mean()
        model.fit(X, y)
        mlflow.log_metric("cv_auc", auc)
        logged_model = mlflow.sklearn.log_model(model, name="model", input_example=X[:5])
        mlflow.log_param("logged_model_uri", logged_model.model_uri)

# COMMAND ----------
# DBTITLE 1,Exercise 3 — find the best run and log its report
best = mlflow.search_runs(
    experiment_ids=[experiment.experiment_id],
    filter_string=f"tags.course_session = '{session_id}'",
    order_by=["metrics.cv_auc DESC", "attributes.start_time ASC"],
    max_results=1,
    output_format="list",
)[0]
best_model_uri = best.data.params["logged_model_uri"]
print(f"Best run: {best.info.run_id} (cv_auc={best.data.metrics['cv_auc']:.4f})")
print(f"Best model URI: {best_model_uri}")

with mlflow.start_run(run_id=best.info.run_id):
    mlflow.log_text(f"Best cv_auc: {best.data.metrics['cv_auc']}", "evaluation_report.txt")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 4 (optional) — register to Unity Catalog
# MAGIC
# MAGIC ```python
# MAGIC # Register the URI returned by mlflow.sklearn.log_model for the best run.
# MAGIC mlflow.set_registry_uri("databricks-uc")
# MAGIC mlflow.register_model(best_model_uri, "YOUR_CATALOG.YOUR_SCHEMA.playbook_classifier")
# MAGIC # Registration requires Unity Catalog privileges to create/use the model and
# MAGIC # create versions. Setting an alias also requires ownership of the registered model.
# MAGIC ```
# MAGIC An alias such as `@champion` follows the approved version when it is reassigned.
# MAGIC Setting an alias requires ownership of the model, `USE CATALOG`, and `USE SCHEMA`.
