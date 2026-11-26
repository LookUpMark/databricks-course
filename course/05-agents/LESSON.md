# Assignment 05 — Custom agents with LangChain and MLflow

## Before you start
Open the notebook on supported Databricks compute. Run the dependency setup cell and allow the Python restart to finish before continuing. Use the same catalog and schema as [topic 03](../03-genie/LESSON.md). Choose an approved Unity Gateway chat model service that supports tool calling, then enter its exact endpoint/service name in the `chat_endpoint` widget. Use the name supplied by your workspace administrator or shown for the approved service; do not enter the workspace URL or a model-family label. If no approved endpoint name is available, ask your administrator before continuing. The notebook routes requests through Unity Gateway with `use_ai_gateway=True`. The notebook pins the LangChain stack to a [compatible version set](https://docs.databricks.com/aws/en/agents/custom-agents/create-custom-tool).

## Walkthrough
1. Run the tool cell and inspect the function and its input/output schema. The example tool counts the synthetic `orders` rows.
2. Run the agent construction cell. Check how the tool is registered and how the Unity Gateway model service is selected. If the model service is unavailable, confirm its exact name and your Unity Catalog permissions with your workspace administrator. Do not embed credentials in code.
3. Run the logging cell to invoke the agent on the example question and log it to MLflow with tracing enabled. Confirm the responses use the tool where appropriate.
4. Open the experiment using the printed path and select **Traces**. Find the invocation and verify that it contains a model span and a tool span. Use the printed run ID to locate the MLflow run separately. See [viewing a trace](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/overview#get-your-first-trace).
5. If you separately log a deployable agent artifact, you can also record its model URI. Registration is optional and requires Unity Catalog model privileges.
6. Add a Markdown cell with the run link, trace evidence, one tool-grounded answer, and a production plan covering tools, prompt constraints, and evaluation criteria.

## Check your work
The query reports five rows for the topic 03 data. The trace includes a model call and a tool call.

## Deliverable
Record the MLflow run link, the trace link or ID if available, one tool-grounded answer, and a short plan for a production agent's tools, prompts, and evaluation.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use a supported Databricks notebook runtime with the required agent packages and an enabled Unity Gateway chat model service that supports tool calling. The identity needs `USE CATALOG`, `USE SCHEMA`, and `SELECT` for `orders`, permission to execute the model service, and permission to create an MLflow experiment under its own `/Users/<current-user>/` folder. Run cells top to bottom; expect a tool-grounded row count and an MLflow run. In **Machine Learning → Experiments**, select **Traces** on the experiment and inspect the spans. Remove only your experiment after retaining evidence. LangChain autologging captures traces in this lab. For a new deployment, use the [Agent Bricks CLI and Agent Runtime](../12-agent-bricks/LESSON.md).
