# Databricks notebook source

# MAGIC %md
# MAGIC # Assignment 04 — Genie as an agent tool
# MAGIC
# MAGIC Use the Genie space from topic 03. Set the space ID widget before running the request.

# COMMAND ----------

import time
from uuid import UUID

import requests

dbutils.widgets.text("genie_space_id", "")
SPACE_ID = dbutils.widgets.get("genie_space_id").strip()

# COMMAND ----------

# DBTITLE 1,Authenticate the HTTP client
HOST = spark.conf.get("spark.databricks.workspaceUrl").removeprefix("https://").rstrip("/")
SESSION = requests.Session()
try:
    context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    SESSION.headers["Authorization"] = f"Bearer {context.apiToken().get()}"
except Exception:  # noqa: BLE001 - notebook authentication varies by compute
    raise RuntimeError("Notebook authentication is unavailable on this compute. See LESSON.md.") from None


def _call(method: str, path: str, payload: dict | None = None, timeout: float = 20) -> dict:
    """Send an authenticated Genie API request and decode the response."""
    response = SESSION.request(method, f"https://{HOST}/api/2.0/genie/{path}", json=payload, timeout=timeout)
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

# DBTITLE 1,Ask about monthly paid revenue
UUID(SPACE_ID)
started = _call("POST", f"spaces/{SPACE_ID}/start-conversation", {"content": "What is the monthly paid revenue?"})
conversation, message = started["conversation"], started["message"]
conversation_id = conversation.get("conversation_id") or conversation["id"]
message_id = message.get("message_id") or message["id"]
path = f"spaces/{SPACE_ID}/conversations/{conversation_id}/messages/{message_id}"
print(_format_message(_poll_message(path)))

# COMMAND ----------

# DBTITLE 1,Exercise — implement the ask_genie tool
def ask_genie(question: str, space_id: str = SPACE_ID) -> str:
    """Send an analytics question and return the answer and generated SQL.

    Args:
        question: A natural-language analytics question.
        space_id: The space identifier for both the conversation and message calls.

    Returns:
        The answer and SQL attachments when available.
    """
    raise NotImplementedError("Generalize the guided cell to take a question and a space ID.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Deliverable
# MAGIC
# MAGIC Keep the API output. Complete `ask_genie` with the same `space_id` in both URLs.
# MAGIC In a Markdown cell, describe when an agent would call Genie versus a document retriever.
