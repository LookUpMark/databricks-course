# Assignment 08 — Medallion ETL

## Before you start
Run the notebook in order. It creates sample tables in the scratch schema; verify the catalog/schema widgets before executing write cells.

## Walkthrough
1. Run the bronze cell to create the table and insert events whose `event_id` is new. Inspect the row count and check that the original JSON is preserved.
2. Run the silver cell. Review the transformations: type casting, invalid-record filtering, and deduplication by key. Compare its count and schema with bronze.
3. Run the gold `MERGE` cell. Confirm the aggregate/upsert output and note the fully qualified table name and row count.
4. Run the time-travel cell and compare the row counts. The cell captures the bronze version and queries it for you; no manual SQL is needed. On a first run in an empty lab schema, the saved bronze version has zero rows and the current version has four. On a rerun with the same events, both have four. If you write a manual `VERSION AS OF` query, replace `<saved-version>` with the integer version you recorded and omit the angle brackets.
5. Read the Auto Loader note. For production, identify a durable checkpoint location unique to the stream; do not use a temporary local path. State the durable `schemaLocation` and `checkpointLocation` paths under the [topic 02 volume](../02-unity-catalog/LESSON.md) named `playbook_files` and the pipeline identity permissions (`READ VOLUME`, `WRITE VOLUME`). Replace `<catalog>` and `<schema>` in the example paths with the widget values when recording them. This is a design exercise only; do not configure or run Auto Loader.
6. Add a Markdown cell with the bronze, silver, and gold table names, row counts, and proposed checkpoint path.

## Check your work
All three medallion layers exist, silver is cleaned/deduplicated, gold contains the expected aggregate, and time travel reads an earlier version.

## Deliverable
Record the three fully qualified table names and row counts, plus one sentence naming the Auto Loader checkpoint location.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use a pre-created writable Unity Catalog schema; the identity needs catalog/schema usage and table create/write/read privileges. Reruns are idempotent for the fixed event IDs. Expected rows: bronze 4, silver 2 (latest valid event per customer), gold 2 aggregates. `DESCRIBE HISTORY` returns newest first, so save the version before a write when demonstrating before/after time travel; read it later with `VERSION AS OF <saved-version>`. Architecture design only (do not configure or run Auto Loader in this lab): use the existing topic 02 `/Volumes/<catalog>/<schema>/playbook_files` volume. The pipeline identity needs `READ VOLUME` and `WRITE VOLUME` on it. Persist `cloudFiles.schemaLocation` and `checkpointLocation` in separate durable subpaths, unique to each stream, for example `/Volumes/<catalog>/<schema>/playbook_files/autoloader/schemas/bronze_events` and `/Volumes/<catalog>/<schema>/playbook_files/autoloader/checkpoints/bronze_events`. A checkpoint preserves offsets and state for recovery; exactly-once processing depends on source and sink semantics plus idempotent writes. Delete only assignment tables you own; dropping a table removes its accessible Delta history.
