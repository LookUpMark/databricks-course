# Assignment 04 — Genie as an Agent Tool

## Before you start
Complete Assignment 03 and have its Genie space ID available. Set the notebook widget to that ID. Use Databricks notebook authentication and a supported `requests` client; never paste a personal access token into notebook source or output. The caller needs permission to use the space. The example uses synthetic data from Assignment 03.

## Walkthrough
1. Copy the space ID from the Genie space URL or its settings page and enter it in the notebook widget.
2. Run the API cell. It starts a conversation, polls until `COMPLETED` or another terminal status, and extracts text and SQL from attachments. A terminal `FAILED` status or poll timeout is an error; inspect the sanitized error and retry only after addressing it.
3. If the request fails, confirm the space ID, workspace host, and that your identity can use the space. If notebook authentication is unavailable on your compute, try workspace-approved compute or record the limitation and review the code and reference answer in `solution.py`. Do not expose credentials when troubleshooting. See the [Get conversation message API](https://docs.databricks.com/api/genie/v1/genie-get-conversation-message).
4. Complete `ask_genie(question, space_id)` using the guided cell. Trim the input, use the same space ID in both API calls, and return readable text and SQL. Try one question, then compare with the [worked solution](solution.py).
5. In a Markdown cell, sketch an agent that routes analytical questions to Genie and document questions to a RAG retriever. State how the agent would decide which tool to call and how it would show the generated SQL for verification.

## Check your work
A successful question produces a completed Genie response; the completed tool stub accepts a question and returns its answer.

## Deliverable
Keep the successful API output, complete `ask_genie`, and document how Genie and RAG would divide question types in one agent.

## Cleanup
The request adds a conversation to your Genie space. Delete the conversation from the Genie interface if you no longer need it. Remove the Genie space only if you own it and no longer need it.
