# Databricks notebook source
# Assignment 12 - Agent Bricks (agent developer platform).
# Lesson recap + verification that the CLI loop has deployed an agent app.
# The build itself happens on the CLI (`agentbricks init/dev/deploy`) — see README;
# this notebook is the inspection half.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 12 — Agent Bricks
# MAGIC
# MAGIC **Goal**: understand the platform and verify that the deployment exists.
# MAGIC
# MAGIC The Agent Bricks CLI (Beta) scaffolds custom agents from LangGraph or OpenAI Agents
# MAGIC SDK templates, runs them locally, and can optionally deploy them to the Databricks
# MAGIC agent runtime. Its exact behavior and availability are workspace dependent.
# MAGIC Authenticate to the intended workspace using the named Databricks CLI profile; there is
# MAGIC no separate workspace-switch command in this flow. Deployment is optional and depends on
# MAGIC workspace access and explicit authorization.
# MAGIC
# COMMAND ----------
# MAGIC %md
# MAGIC ## Lesson recap
# MAGIC
# MAGIC | Layer | Component |
# MAGIC |---|---|
# MAGIC | Build loop | `agentbricks init` → `dev` → `deploy` |
# MAGIC | Source of truth | `agent.toml` (resources: memory, sessions, tools, tracing) |
# MAGIC | Compute | Agent Runtime on Databricks Apps (`DurableAgentServer`) |
# MAGIC | Configuration | `agent.toml` declares managed resource and tool bindings |
# MAGIC | Local run | `agentbricks dev` starts a local server on port 8000 |
# MAGIC | Deployment | Optional `agentbricks deploy my-agent`; provisions declared resources |
# MAGIC
# MAGIC Never claim a live deployment unless the command completed and returned an actual URL.
# MAGIC
# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise — CLI steps (run in a terminal)
# MAGIC
# MAGIC ```bash
# MAGIC uv tool install databricks-agentbricks
# MAGIC databricks auth login --host "https://<your-workspace-url>" --profile course
# MAGIC agentbricks login --profile course
# MAGIC agentbricks init --framework langgraph my-agent
# MAGIC cd my-agent && agentbricks dev  # local loop, localhost:8000
# MAGIC # Optional, only when authorized and permitted: agentbricks deploy my-agent
# MAGIC ```
# MAGIC
# MAGIC Consult the linked official CLI guide for exact current options, auth behavior, and
# MAGIC generated `agent.toml`. Never include `.env` values or credentials in notebook outputs.
# MAGIC
# COMMAND ----------
# DBTITLE 1,Optional observation — check an actual deployed app in the UI
# COMMAND ----------
# MAGIC %md
# MAGIC Deployment is optional. If you deployed with authorization, record the actual returned URL
# MAGIC and inspect the app in **Databricks Apps**. If you did not deploy, record “not deployed”.


# COMMAND ----------
# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC 1. Record local run status and, only if actually deployed, the returned URL.
# MAGIC 2. Include a safe, redacted `agent.toml` excerpt — it declares managed resources and
# MAGIC    tool bindings. Do not copy secrets.
# MAGIC 3. One paragraph: which tools/context would this agent get (Genie? RAG? UC
# MAGIC    functions? MCP?) and what it would never be allowed to do.
