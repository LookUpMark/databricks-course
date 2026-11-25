# Databricks notebook source

# MAGIC %md
# MAGIC # Assignment 04 — Worked solution
# MAGIC
# MAGIC Use the Genie Agent from topic 03. The Chat mode API retains its `/spaces/{space_id}` path, so set the agent ID in the `genie_space_id` widget.

# COMMAND ----------

import time
from uuid import UUID

import requests
from databricks.sdk import WorkspaceClient

dbutils.widgets.text("genie_space_id", "")
SPACE_ID = dbutils.widgets.get("genie_space_id").strip()

# COMMAND ----------

# DBTITLE 1,Authenticate the HTTP client
WORKSPACE = WorkspaceClient()
HOST = WORKSPACE.config.host.rstrip("/")
SESSION = requests.Session()


def _call(method: str, path: str, payload: dict | None = None, timeout: float = 20) -> dict:
    """Send an authenticated Genie API request and decode the response."""
    response = SESSION.request(
        method,
        f"{HOST}/api/2.0/genie/{path}",
        headers=WORKSPACE.config.authenticate(),
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def _poll_message(path: str, timeout: float = 90) -> dict:
    """Wait for a completed Genie message or report a failure or timeout."""
    deadline = time.monotonic() + timeout
    while (remaining := deadline - time.monotonic()) > 0:
        message = _call("GET", path, timeout=min(20, remaining))
        status = message.get("status")
        if status == "COMPLETED":
            return message
        if status in {"FAILED", "CANCELLED", "QUERY_RESULT_EXPIRED"}:
            raise RuntimeError(f"Genie ended with {status}. Open the Genie conversation to inspect its details.")
        time.sleep(max(0, min(2, deadline - time.monotonic())))
    raise TimeoutError(f"Genie did not complete within {timeout:g} seconds.")


def _format_message(message: dict) -> str:
    """Extract the answer and generated SQL from Genie attachments."""
    attachments = message.get("attachments") or []
    answers = [(item.get("text") or {}).get("content") for item in attachments]
    queries = [(item.get("query") or {}).get("query") for item in attachments]
    answer = "\n".join(filter(None, answers)) or "(No text attachment returned.)"
    sql = "\n\n".join(filter(None, queries)) or "(No SQL attachment returned.)"
    return f"Answer:\n{answer}\n\nGenerated SQL:\n{sql}"


# COMMAND ----------


# DBTITLE 1,Implement and call the ask_genie tool
def ask_genie(question: str, space_id: str = SPACE_ID) -> str:
    """Send an analytics question and return the answer and generated SQL.

    Args:
        question: A natural-language analytics question.
        space_id: Genie Agent ID, called space_id by the Chat mode API. Defaults to the notebook widget.

    Returns:
        The answer and SQL attachments when available.
    """
    question, space_id = question.strip(), space_id.strip()
    if not question:
        raise ValueError("Enter an analytics question.")
    UUID(space_id)
    started = _call("POST", f"spaces/{space_id}/start-conversation", {"content": question})
    conversation, message = started["conversation"], started["message"]
    conversation_id = conversation.get("conversation_id") or conversation["id"]
    message_id = message.get("message_id") or message["id"]
    path = f"spaces/{space_id}/conversations/{conversation_id}/messages/{message_id}"
    return _format_message(_poll_message(path))


print(ask_genie("What is the monthly paid revenue?", SPACE_ID))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example deliverable
# MAGIC
# MAGIC On the synthetic orders in Topic 03, the reference SQL groups by year and month
# MAGIC and filters to `status = 'paid'`. Expected values are 100 EUR in January, 250 EUR
# MAGIC in February, and 120 EUR in April 2026. Compare those values with your Genie result
# MAGIC and inspect the SQL returned above.
# MAGIC
# MAGIC Route structured questions such as monthly revenue to Genie. Route questions
# MAGIC about written policy or definitions to document retrieval.
