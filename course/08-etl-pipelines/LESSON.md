# Assignment 08 — Medallion ETL

## Before you start
Open the [assignment notebook](databricks_notebook_source.py), set its `catalog` and `schema` widgets to your pre-created writable scratch schema, then run the cells in order. The notebook creates sample tables in that schema; verify the widget values before executing write cells. Any `<catalog>` and `<schema>` shown in example table names stand for those widget values; replace them and omit the angle brackets.

## Walkthrough
1. Run **Exercise 1 — bronze: raw data as it lands**. It creates `<catalog>.<schema>.bronze_events` and inserts only unseen `event_id` values. Inspect the row count and confirm the original JSON is preserved in `raw`.
2. Run **Exercise 2 — silver: clean, dedupe, type**. It writes `<catalog>.<schema>.silver_events`; review type casting, invalid-record filtering, whitespace trimming, and keeping the latest valid event per `id`. Compare its count and schema with bronze.
3. Run **Exercise 3 — gold: MERGE into aggregate**. It upserts per-customer totals into `<catalog>.<schema>.gold_customer_totals`. Confirm the aggregate output and note the fully qualified name and row count.
4. Run the time-travel cell and compare the row counts. The cell captures the bronze version and queries it for you; no manual SQL is needed. On a first run in an empty lab schema, the saved bronze version has zero rows and the current version has four. On a rerun with the same events, both have four. If you write a manual `VERSION AS OF` query, replace `<saved-version>` with the integer version you recorded and omit the angle brackets.
5. Read the Auto Loader note. For production, identify a durable checkpoint location unique to the stream; do not use a temporary local path. State the durable `schemaLocation` and `checkpointLocation` paths under the [topic 02 volume](../02-unity-catalog/LESSON.md) named `playbook_files` and the pipeline identity permissions (`READ VOLUME`, `WRITE VOLUME`). Replace `<catalog>` and `<schema>` in the example paths with the widget values when recording them. This is a design exercise only; do not configure or run Auto Loader.
6. Add a Markdown cell with the three fully qualified names (`bronze_events`, `silver_events`, and `gold_customer_totals`), their row counts, and the proposed checkpoint path. On a clean first run, expect 4 bronze, 2 silver, and 2 gold rows.

## Check your work
All three medallion layers exist, silver is cleaned/deduplicated, gold contains the expected aggregate, and time travel reads an earlier version.

## Deliverable
Record the three fully qualified table names and row counts, plus one sentence naming the Auto Loader checkpoint location.

## Worked solution
See [solution.py](solution.py) for a complete example with an example deliverable. Replace synthetic links and execution-specific values with evidence from your workspace.

## Access, expected result, and cleanup
Use a pre-created writable Unity Catalog schema; the identity needs catalog/schema usage and table create/write/read privileges. Reruns are idempotent for the fixed event IDs. Expected rows: bronze 4, silver 2 (latest valid event per customer), gold 2 aggregates. `DESCRIBE HISTORY` returns newest first, so save the version before a write when demonstrating before/after time travel; read it later with `VERSION AS OF <saved-version>`. Architecture design only (do not configure or run Auto Loader in this lab): use the existing topic 02 `/Volumes/<catalog>/<schema>/playbook_files` volume. The pipeline identity needs `READ VOLUME` and `WRITE VOLUME` on it. Persist `cloudFiles.schemaLocation` and `checkpointLocation` in separate durable subpaths, unique to each stream, for example `/Volumes/<catalog>/<schema>/playbook_files/autoloader/schemas/bronze_events` and `/Volumes/<catalog>/<schema>/playbook_files/autoloader/checkpoints/bronze_events`. A checkpoint preserves offsets and state for recovery; exactly-once processing depends on source and sink semantics plus idempotent writes. Delete only assignment tables you own; dropping a table removes its accessible Delta history.
