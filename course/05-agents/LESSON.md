# Assignment 05 — Custom agents with LangChain and MLflow

## Before you start
Open the notebook on supported Databricks compute. Run the dependency setup cell and allow the Python restart to finish before continuing. Use the same catalog and schema as [topic 03](../03-genie/LESSON.md). Choose an approved chat model endpoint that supports tool calling, then enter its name in the `chat_endpoint` widget. The notebook pins the LangChain stack to a [compatible version set](https://docs.databricks.com/aws/en/agents/custom-agents/create-custom-tool).

## Walkthrough
1. Run the tool cell and inspect the function and its input/output schema. The example tool counts the synthetic `orders` rows.
2. Run the agent construction cell. Check how the tool is registered and how the model endpoint is selected. If the endpoint is unavailable, use an endpoint approved for your workspace and avoid embedding credentials in code.
3. Run the logging cell to invoke the agent on the example question and log it to MLflow with tracing enabled. Confirm the responses use the tool where appropriate.
4. Use the printed experiment path and run ID to open the run. In the run page, inspect the trace and verify that the model call and tool call are represented.
5. Registration is optional and may require Unity Catalog permissions. This lab logs a trace rather than a registered model. Record a model URI only if you separately log a deployable agent artifact.
6. Add a Markdown cell with the run link/model URI, one tool-grounded question, and a production plan covering tools, prompt constraints, and evaluation criteria.

## Check your work
The query reports five rows for the topic 03 data and the trace includes a model call and a tool call; record a model URI only if you separately log a model artifact or register it.

## Deliverable
Record the MLflow run link/model URI, one tool-grounded answer, and a short plan for a production agent's tools, prompts, and evaluation.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use a supported Databricks notebook runtime with the required agent packages and an enabled chat model serving endpoint. The identity needs `USE CATALOG`, `USE SCHEMA` and `SELECT` for `orders`, `CAN QUERY` on the model endpoint, and permission to create an MLflow experiment under its own `/Users/<current-user>/` folder. Run cells top to bottom; expect a tool-grounded row count and an MLflow run. In **Machine Learning → Experiments**, open the experiment and run, then inspect trace spans for model and tool calls. Remove only your experiment after retaining evidence. LangChain autologging captures traces in this lab. For a new deployment, use the [Agent Bricks CLI and Agent Runtime](../12-agent-bricks/LESSON.md).
