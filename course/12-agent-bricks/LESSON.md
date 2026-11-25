# Assignment 12 — Agent Bricks

Worked example: [solution notebook](solution.py).

## Before you start
Use a terminal with Python 3.11+, `uv`, Databricks CLI authentication, and access to the Agent Bricks feature. The Agent Bricks CLI is documented as Beta. Deployment provisions declared resources and rolls out an agent, so deployment is optional and must be explicitly permitted for your assigned development workspace. See the [official Agent Bricks CLI guide](https://docs.databricks.com/aws/en/agents/custom-agents/agent-bricks-cli).

## Walkthrough
1. Install with `uv tool install databricks-agentbricks`, then authenticate using the workspace host and a named profile: `databricks auth login --host https://<workspace-url> --profile course`; then `agentbricks login --profile course`.
2. From an empty working directory, scaffold a LangGraph project with `agentbricks init --framework langgraph my-agent`. Open `agent.toml` and identify declared resources and tools. Do not paste `.env`, tokens, or generated secrets into the notebook.
3. Enter the project directory and run `agentbricks dev`. Open the local chat UI at `http://localhost:8000`; send a test prompt and confirm the agent responds. Stop the local server when finished.
4. Optional: deploy only when authorized, using the documented `agentbricks deploy my-agent`. This provisions declared resources and returns a URL. If deploying, record the actual URL and status; never invent one.
5. For a deployed agent, open **Apps** in the workspace navigation and find its actual app entry (the guide documents the `agent-bricks-<name>` naming pattern). Confirm status and open the listed URL. Otherwise record “not deployed” and why.
6. Include a redacted, safe excerpt of `agent.toml` (omit secrets and replace generated IDs/names as needed). Add a governance note naming allowed tools/context and prohibited actions.

## Check your work
The local agent responds. If optional deployment was authorized and completed, its actual URL opens; otherwise the deliverable clearly says no deployment occurred.

## Deliverable
Record the deployment URL or the reason deployment was unavailable, include `agent.toml`, and describe allowed context/tools and prohibited actions.
