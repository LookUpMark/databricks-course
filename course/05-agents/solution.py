# Databricks notebook source
# Assignment 05 — Custom agents with LangChain and MLflow.
# Builds a minimal tool-calling agent with LangGraph + traces, and logs it to MLflow.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 05 — Agents
# MAGIC
# MAGIC **Goal**: build, trace and log a minimal tool-calling agent and inspect its LangChain/LangGraph traces in MLflow.

# COMMAND ----------
# DBTITLE 1,Install agent dependencies (serverless/classic)
# MAGIC %pip install -q "langchain==1.2.10" "langgraph==1.0.10" "langgraph-prebuilt==1.0.8" "databricks-langchain==0.22.0" "mlflow[databricks]==3.18.0"
# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------
import re

dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
dbutils.widgets.text("chat_endpoint", defaultValue="")
# COMMAND ----------

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
from langchain.agents import create_agent

scratch_table = f"{catalog}.{schema}.orders"
llm = ChatDatabricks(model=endpoint, use_ai_gateway=True)
agent = create_agent(llm, tools=[sql_lookup])

# COMMAND ----------
# DBTITLE 1,Exercise 3 — log the agent to MLflow with tracing
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
print("Open the experiment in Machine Learning → Experiments and select Traces.")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 4 — deployment and evaluation design
# MAGIC
# MAGIC - This example logs a run and agent traces. Use them to verify the model's call to the SQL tool.
# MAGIC - For a new deployment, use the Agent Bricks CLI and Agent Runtime described in topic 12.
# MAGIC - Evaluate a packaged agent on a golden set using supported MLflow evaluation
# MAGIC   APIs and workspace judges; exact options depend on the installed runtime.
# MAGIC
# MAGIC ## Deliverable
# MAGIC
# MAGIC In a Markdown cell, record the MLflow run link, the trace link or ID if available, and one
# MAGIC tool-grounded question and answer. Add a short production plan covering tools, prompts, and
# MAGIC evaluation criteria. Include a model URI only if you separately logged a deployable artifact.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Worked deliverable (example)
# MAGIC
# MAGIC Run URL: find the printed run ID in the experiment. Trace evidence: open the invocation in Traces and record its link or ID if available.
# MAGIC Example-only URL shape: `https://<workspace>/ml/experiments/<experiment-id>/runs/<run-id>` (synthetic; replace with the real link).
# MAGIC Example tool-grounded question: “How many rows are in `<catalog>.<schema>.orders`?” For the five synthetic orders in topic 03, the expected count is 5. Confirm the SQL tool span before attributing that output to the tool.
# MAGIC Production plan: allow-list tables and columns, use a read-only SQL identity, enforce query timeouts, instruct the model to cite tool results, and evaluate exact count correctness, permission-denial behavior, and prompt-injection resistance on a fixed golden set.
# MAGIC
# MAGIC For a production deployment, adapt the agent using the Agent Bricks CLI in topic 12. Keep the same tool and trace evaluation criteria.
