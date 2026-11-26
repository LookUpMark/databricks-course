# Assignment 04 — Genie as an Agent Tool

## Before you start
Complete Assignment 03 and have the Genie Agent ID available. Open the [assignment notebook](databricks_notebook_source.py) and enter that ID in the `genie_space_id` widget. The widget and Chat mode API still call this a `space_id`: the compatible conversation endpoint is `/api/2.0/genie/spaces/{space_id}/...`, even though the current UI product is named Genie Agents. Use Databricks notebook authentication through `WorkspaceClient` and a supported `requests` client; never paste a personal access token into notebook source or output. The caller needs at least `CAN VIEW` on the Genie Agent and `SELECT` on its Unity Catalog data. The example uses synthetic data from topic 03.

The separate [Agent mode API](https://docs.databricks.com/api/genie/v1/agent-mode-create-response) streams responses through `/api/2.0/genie/agents/{agent_id}/responses`. The exercise demonstrates Chat mode with polling.

## Walkthrough
1. Copy the raw agent ID (UUID) from its workspace URL or settings page and enter only that ID in the `genie_space_id` notebook widget. The API path `/spaces/{space_id}/...` is documentation notation: the braces are not part of the ID or a value to paste. The endpoint retains the legacy “space” name for compatibility.
2. Run the first API cell to send its sample question, “What is the monthly paid revenue?” It polls until `COMPLETED` or another terminal status, then prints the answer and generated SQL. Compare monthly paid amounts with topic 03 (EUR 100 in January, EUR 250 in February, and EUR 120 in April 2026). A terminal `FAILED` status or poll timeout is an error; inspect the sanitized error and retry only after addressing it.
3. If the request fails, confirm the agent ID, workspace host, and that your identity can use the agent. If SDK notebook authentication is unavailable on your compute, use workspace-approved compute or record the limitation and review the code and reference answer in `solution.py`. Do not expose credentials when troubleshooting. See the [Get conversation message API](https://docs.databricks.com/api/genie/v1/genie-get-conversation-message).
4. In the `ask_genie` cell, replace `raise NotImplementedError` with the request/poll/format flow from the preceding cell. Validate the ID with `UUID`, trim the question and ID, use that same ID in the start-conversation and message URLs, poll the returned message until completion, and return readable answer and SQL attachments. Test it with `ask_genie("What is the monthly paid revenue?")`, then compare with the [worked solution](solution.py).
5. In a Markdown cell, sketch an agent that routes analytical questions to Genie and document questions to a RAG retriever. State how the agent would decide which tool to call and how it would show the generated SQL for verification.

## Check your work
A successful question produces a completed Genie response; the completed tool stub accepts a question and returns its answer.

## Deliverable
Keep the successful API output, complete `ask_genie`, and document how Genie and RAG would divide question types in one agent.

## Cleanup
The request adds a conversation to your Genie Agent. Delete the conversation from the Genie interface if you no longer need it. Remove the agent only if you own it and no longer need it.
