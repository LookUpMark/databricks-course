# Assignment 08 — Medallion ETL

## Before you start
Run the notebook in order. It creates sample tables in the scratch schema; verify the catalog/schema widgets before executing write cells.

## Walkthrough
1. Run the bronze cell to create/append raw records. Inspect the table and note its row count and raw shape.
2. Run the silver cell. Review the transformations: type casting, invalid-record filtering, and deduplication by key. Compare its count and schema with bronze.
3. Run the gold `MERGE` cell. Confirm the aggregate/upsert output and note the fully qualified table name and row count.
4. Run the time-travel cell. Compare the historical version with the current table and describe the difference.
5. Read the Auto Loader note. For production, identify a durable checkpoint location unique to the stream; do not use a temporary local path. State the durable `schemaLocation` and `checkpointLocation` paths and the volume permissions required.
6. Add a Markdown cell with the bronze, silver, and gold table names, row counts, and proposed checkpoint path.

## Check your work
All three medallion layers exist, silver is cleaned/deduplicated, gold contains the expected aggregate, and time travel reads an earlier version.

## Deliverable
Record the three fully qualified table names and row counts, plus one sentence naming the Auto Loader checkpoint location.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use a pre-created writable Unity Catalog schema; the identity needs catalog/schema usage and table create/write/read privileges. Reruns are idempotent for the fixed event IDs. Expected rows: bronze 4, silver 2 (latest valid event per customer), gold 2 aggregates. `DESCRIBE HISTORY` returns newest first, so save the version before a write when demonstrating before/after time travel; read it later with `VERSION AS OF <saved-version>`. For production Auto Loader, persist `cloudFiles.schemaLocation` and `checkpointLocation` in separate durable storage locations, unique to each stream. A checkpoint preserves offsets and state for recovery; exactly-once processing depends on source and sink semantics plus idempotent writes. Delete only assignment tables you own; dropping a table removes its accessible Delta history.
