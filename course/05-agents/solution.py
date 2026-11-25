# Databricks notebook source
# Assignment 05 - Agents (Mosaic AI Agent Framework).
# Builds a minimal tool-calling agent with LangGraph + traces, and logs it to MLflow.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 05 — Agents
# MAGIC
# MAGIC **Goal**: build, trace and log a minimal tool-calling agent and inspect its LangChain/LangGraph traces in MLflow.

# COMMAND ----------
# DBTITLE 1,Install agent dependencies (serverless/classic)
# COMMAND ----------
# MAGIC %pip install -q "langchain==1.2.10" "langgraph==1.0.10" "langgraph-prebuilt==1.0.8" "databricks-langchain==0.22.0" "mlflow[databricks]==3.18.0"
# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------
import re

dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
dbutils.widgets.text("chat_endpoint", defaultValue="")
endpoint = dbutils.widgets.get("chat_endpoint").strip()
if not endpoint:
    raise ValueError("Enter a workspace-approved chat model serving endpoint that supports tool calling.")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not catalog or not schema:
    raise ValueError("Set catalog and schema widgets to your pre-created writable Unity Catalog schema.")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("catalog and schema must be simple Unity Catalog identifiers (letters, digits, underscores).")

# COMMAND ----------
# DBTITLE 1,Exercise 1 — a simple tool
# COMMAND ----------
from databricks_langchain import ChatDatabricks
from langchain_core.tools import tool


@tool
def sql_lookup(table: str) -> str:
    """Return the row count of a fully-qualified Delta table.

    Args:
        table: Fully-qualified table name, e.g. ``catalog.schema.table``.

    Returns:
        str: Human-readable row count for the agent to relay.
    """
    if table != scratch_table:
        raise ValueError(f"This exercise only permits querying {scratch_table}.")
    n = spark.sql(f"SELECT COUNT(*) AS n FROM `{catalog}`.`{schema}`.orders").first().n
    return f"Table {table} has {n} rows."


# COMMAND ----------
# DBTITLE 1,Exercise 2 — minimal agent
# COMMAND ----------
from langchain.agents import create_agent

scratch_table = f"{catalog}.{schema}.orders"
llm = ChatDatabricks(endpoint=endpoint)
agent = create_agent(llm, tools=[sql_lookup])

# COMMAND ----------
# DBTITLE 1,Exercise 3 — log the agent to MLflow with tracing
# COMMAND ----------
import mlflow

user = spark.sql("SELECT current_user()").first()[0]
experiment = mlflow.set_experiment(f"/Users/{user}/databricks-course-agents")
print(f"Experiment: {experiment.name}")
mlflow.langchain.autolog()

with mlflow.start_run(run_name="assignment-05-react-agent") as active_run:
    mlflow.set_tag("assignment", "05-agents")
    mlflow.set_tag("tools", "sql_lookup")
    mlflow.log_param("endpoint", endpoint)
    result = agent.invoke(
        {"messages": [("user", f"How many rows are in {scratch_table}?")]},
        config={"configurable": {"thread_id": "assignment-05"}},
    )
    print(result["messages"][-1].content)
    run_id = active_run.info.run_id

run = mlflow.get_run(run_id)
print(f"Run id: {run_id}")
print(f"Experiment id: {run.info.experiment_id}")
print("Open the experiment from Machine Learning → Experiments and inspect the trace.")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 4 — registration & evaluation (documented)
# MAGIC
# MAGIC - This example creates a traced MLflow run; it does not log a model artifact,
# MAGIC   so `runs:/{run_id}/model` is not available from this notebook as written.
# MAGIC - To serve it, implement and log the documented ChatAgent interface, validate
# MAGIC   its model signature/dependencies, then register the resulting logged URI.
# MAGIC - Evaluate a packaged agent on a golden set using supported MLflow evaluation
# MAGIC   APIs and workspace judges; exact options depend on the installed runtime.
# MAGIC
# MAGIC ## Deliverable
# MAGIC
# MAGIC Add a markdown cell with: the MLflow run link (and a model URI only if you separately log a model artifact), one question the agent answered
# MAGIC using its tool, and a short plan (tools, prompts, eval criteria) for a real
# MAGIC production agent.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Worked deliverable (example)
# MAGIC
# MAGIC Run URL: open the printed run id under Machine Learning → Experiments.
# MAGIC Example-only URL shape: `https://<workspace>/ml/experiments/<experiment-id>/runs/<run-id>` (synthetic; replace with the real link).
# MAGIC Example tool-grounded question: “How many rows are in `<catalog>.<schema>.orders`?” For the five synthetic orders in topic 03, the expected count is 5. Confirm the SQL tool span before attributing that output to the tool.
# MAGIC Production plan: allow-list tables and columns, use a read-only SQL identity, enforce query timeouts, instruct the model to cite tool results, and evaluate exact count correctness, permission-denial behavior, and prompt-injection resistance on a fixed golden set.
# MAGIC
# MAGIC MLflow LangChain autologging can capture LangChain/LangGraph calls and traces when supported by the installed MLflow integration. That is tracing coverage; it does not automatically package a serving-ready Databricks `ChatAgent` interface. For serving, implement and log the documented `mlflow.pyfunc.ChatAgent` contract (including `predict` and, when required, `predict_stream`) and verify the model signature/dependencies in your workspace runtime.
