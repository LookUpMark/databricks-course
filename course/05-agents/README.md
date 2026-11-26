# Assignment 05 — Custom agents with LangChain and MLflow

Build, trace, and log a minimal tool-calling agent.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- Executed notebook: agent answers a question using its tool, trace visible.
- MLflow run link and trace evidence in a Markdown cell. Include a model URI only if you separately logged a deployable agent artifact.
- Short markdown plan (tools, prompts, eval criteria) for a real production agent.

## Access, expected result, and cleanup
Use a supported Databricks notebook runtime with the required agent packages and an enabled chat model serving endpoint that supports tool calling. The identity needs `USE CATALOG`, `USE SCHEMA` and `SELECT` for `orders`, `CAN QUERY` on the model endpoint, and permission to create an MLflow experiment under its own `/Users/<current-user>/` folder. Run cells top to bottom; expect a tool-grounded row count and an MLflow run. In **Machine Learning → Experiments**, open the experiment and select **Traces** to inspect spans for model and tool calls. Remove only your experiment after retaining evidence. LangChain autologging captures traces in this lab. For a new deployment, use the [Agent Bricks CLI and Agent Runtime](../12-agent-bricks/LESSON.md).
