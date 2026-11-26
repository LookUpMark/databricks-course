# Assignment 12 — Agent Bricks

Worked example: [solution notebook](solution.py).

## Before you start
Open the [companion notebook](databricks_notebook_source.py) for the inspection deliverable. Use a terminal with Python 3.11+, `uv`, Databricks CLI authentication, and access to the Agent Bricks feature for the build steps. The Agent Bricks CLI is documented as Beta. Deployment provisions declared resources and rolls out an agent, so deployment is optional and must be explicitly permitted for your assigned development workspace. See the [official Agent Bricks CLI guide](https://docs.databricks.com/aws/en/agents/custom-agents/agent-bricks-cli).

## Walkthrough
1. Install with `uv tool install databricks-agentbricks`, then authenticate using the workspace host and a named profile: `databricks auth login --host "https://<workspace-url>" --profile course`; then `agentbricks login --profile course`. Replace `<workspace-url>` with the host from your Databricks workspace URL, keeping `https://` and the quotes; do not include angle brackets. `course` is the profile name used in the following commands. The CLI is Beta. These commands select/authenticate the target workspace profile; there is no separate workspace-switch step. Feature availability depends on the workspace.
2. From an empty working directory, scaffold a LangGraph project with `agentbricks init --framework langgraph my-agent`. Here `my-agent` is a literal example project name; keep it for the next commands or replace it consistently. Open `agent.toml` inside the generated project directory and identify its declared resources and tools. Do not paste `.env`, tokens, or generated secrets into the notebook.
3. Enter that project directory and run `agentbricks dev`. Wait for the CLI to report that the local server is ready, then open `http://localhost:8000`; send a test prompt and record whether the agent responds. Stop the local server with Ctrl+C when finished.
4. Optional: deploy only when explicitly authorized and permitted in the assigned development workspace, from the project directory, using `agentbricks deploy my-agent` (or the same project name you chose in step 2). Deployment provisions declared resources and returns a URL. If deploying, record the actual URL and status; never invent one. Otherwise record “not deployed” and continue with the local exercise.
5. For a deployed agent, open **Apps** in the workspace navigation and find its actual app entry. With the default project name, look for `agent-bricks-my-agent`; if you chose a different name, use that name. Confirm the status and open the URL shown by the workspace. Otherwise record “not deployed” and why.
6. Include a redacted, safe excerpt of the generated `agent.toml` (omit secrets and replace generated IDs/names as needed). The sample excerpt in the worked solution is illustrative; do not paste it over the generated file. Add a governance note naming allowed tools/context and prohibited actions. Record `not deployed` if you only completed the local run.

## Check your work
The local agent responds. If optional deployment was authorized and completed, its actual URL opens; otherwise the deliverable clearly says no deployment occurred.

## Deliverable
Record the deployment URL or the reason deployment was unavailable, include `agent.toml`, and describe allowed context/tools and prohibited actions.

## Cleanup

Stop any running local `agentbricks dev` process. Keep the generated project as the deliverable. If you deployed with authorization, remove the app and its provisioned resources only through the workspace's supported flow and only after saving evidence and confirming the deployment is no longer needed.
