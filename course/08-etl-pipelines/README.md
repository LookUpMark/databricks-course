# Assignment 08 — Medallion ETL

Transform sample data through bronze, silver, and gold layers.

## Materials

- [Step-by-step lesson](LESSON.md)
- [Databricks notebook](databricks_notebook_source.py)
- [Worked solution notebook](solution.py)

## Exercise and deliverable

Follow the lesson, complete the notebook exercises, and submit the requested evidence:

- Executed notebook with bronze/silver/gold tables in
  `<catalog>.<personal_schema>`.
- A markdown cell listing the three fully-qualified table names and the row counts,
  plus one sentence on where you'd set the Auto Loader checkpoint.

## Access, expected result, and cleanup
Use a pre-created writable Unity Catalog schema; the identity needs catalog/schema usage and table create/write/read privileges. Reruns are idempotent for the fixed event IDs. Expected rows: bronze 4, silver 2 (latest valid event per customer), gold 2 aggregates. `DESCRIBE HISTORY` returns newest first, so save the version before a write when demonstrating before/after time travel; read it later with `VERSION AS OF <saved-version>`. Architecture design only (do not configure or run Auto Loader in this lab): use the existing [topic 02 volume](../02-unity-catalog/LESSON.md) at `/Volumes/<catalog>/<schema>/playbook_files` volume. The pipeline identity needs `READ VOLUME` and `WRITE VOLUME` on it. Persist `cloudFiles.schemaLocation` and `checkpointLocation` in separate durable subpaths, unique to each stream, for example `/Volumes/<catalog>/<schema>/playbook_files/autoloader/schemas/bronze_events` and `/Volumes/<catalog>/<schema>/playbook_files/autoloader/checkpoints/bronze_events`. A checkpoint preserves offsets and state for recovery; exactly-once processing depends on source and sink semantics plus idempotent writes. Delete only assignment tables you own; dropping a table removes its accessible Delta history.
