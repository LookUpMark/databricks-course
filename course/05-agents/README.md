# Assignment 05 — Mosaic AI Agent Framework

Build, trace, and log a minimal tool-calling agent.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- Executed notebook: agent answers a question using its tool, trace visible.
- MLflow run link / model URI recorded in a markdown cell.
- Short markdown plan (tools, prompts, eval criteria) for a real production agent.

## Access, expected result, and cleanup
Use a supported Databricks notebook runtime with the required agent packages and an enabled chat model serving endpoint that supports tool calling. The identity needs permission to query the `orders` table, use the model endpoint, and create an MLflow experiment under its own `/Users/<current-user>/` folder. Run cells top to bottom; expect a tool-grounded row count and an MLflow run. In **Machine Learning → Experiments**, open the experiment and run, then inspect trace spans for model and tool calls. Remove only your experiment after retaining evidence. LangChain autologging traces supported calls; it does not itself guarantee a serving-compatible `ChatAgent` model.
