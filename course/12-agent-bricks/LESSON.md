# Assignment 12 — Agent Bricks

Worked example: [solution notebook](solution.py).

## Before you start
Use a terminal with Python 3.11+, `uv`, Databricks CLI authentication, and access to the Agent Bricks feature. The Agent Bricks CLI is documented as Beta. Deployment provisions declared resources and rolls out an agent, so deployment is optional and must be explicitly permitted for your assigned development workspace. See the [official Agent Bricks CLI guide](https://docs.databricks.com/aws/en/agents/custom-agents/agent-bricks-cli).

## Walkthrough
1. Install with `uv tool install databricks-agentbricks`, then authenticate using the workspace host and a named profile: `databricks auth login --host "https://<workspace-url>" --profile course`; then `agentbricks login --profile course`. Replace `<workspace-url>` with the host from your Databricks workspace URL, keeping `https://` and the quotes; do not include angle brackets. `course` is the profile name used in the following commands. The CLI is Beta. These commands select/authenticate the target workspace profile; there is no separate workspace-switch step. Feature availability depends on the workspace.
2. From an empty working directory, scaffold a LangGraph project with `agentbricks init --framework langgraph my-agent`. Here `my-agent` is a literal example project name; keep it for the next commands or replace it consistently. Open the generated `my-agent/agent.toml` and identify declared resources and tools. Do not paste `.env`, tokens, or generated secrets into the notebook.
3. Enter the project directory and run `agentbricks dev`. Open the local chat UI at `http://localhost:8000`; send a test prompt and confirm the agent responds. Stop the local server when finished.
4. Optional: deploy only when explicitly authorized and permitted in the assigned development workspace, from the project directory, using `agentbricks deploy my-agent` (or the same project name you chose in step 2). Deployment provisions declared resources and returns a URL. If deploying, record the actual URL and status; never invent one. Otherwise record “not deployed” and continue with the local exercise.
5. For a deployed agent, open **Apps** in the workspace navigation and find its actual app entry. With the default project name, look for `agent-bricks-my-agent`; if you chose a different name, use that name. Confirm the status and open the URL shown by the workspace. Otherwise record “not deployed” and why.
6. Include a redacted, safe excerpt of the generated `agent.toml` (omit secrets and replace generated IDs/names as needed). The sample excerpt in the worked solution is illustrative; do not paste it over the generated file. Add a governance note naming allowed tools/context and prohibited actions.

## Check your work
The local agent responds. If optional deployment was authorized and completed, its actual URL opens; otherwise the deliverable clearly says no deployment occurred.

## Deliverable
Record the deployment URL or the reason deployment was unavailable, include `agent.toml`, and describe allowed context/tools and prohibited actions.
