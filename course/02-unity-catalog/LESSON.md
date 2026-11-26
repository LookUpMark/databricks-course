# Assignment 02 — Unity Catalog

## Before you start
Open the [assignment notebook](databricks_notebook_source.py) in the workspace, attach Unity Catalog-compatible compute, and run the setup cells. Enter your assigned catalog and personal scratch schema in the `catalog` and `schema` widgets; both default to empty because the notebook writes objects. You need `USE CATALOG` and `USE SCHEMA`, plus `CREATE TABLE` and `CREATE VOLUME` on the lab schema. Reading and writing files requires `READ VOLUME` and `WRITE VOLUME`, supplied by ownership or grants. See [volume privileges](https://docs.databricks.com/aws/en/volumes/privileges). If the schema already exists and you are allowed to use it, no schema creation privilege is needed. Do not use a production schema.

## Walkthrough
1. In the left sidebar click **Catalog**, select the assigned catalog, and note the current context. In the notebook enter the catalog and personal scratch schema widgets (simple SQL identifiers only).
2. Run the validation/context cell. If the schema exists and access is allowed, use it. If it does not exist and you have `CREATE SCHEMA` on the catalog, open **Catalog → your catalog → Create schema**, enter your unique lab schema name, and save. Otherwise ask your administrator to create it. Confirm the fully qualified schema.
3. Run **Create a managed table with synthetic rows**, then the `DESCRIBE` cells. Confirm the fully qualified `sample_features` table name and that its type is managed. Rerunning overwrites `sample_features`; use a table you own or confirm you have the privileges to replace it.
4. Run the grants cell. Review the effective privileges returned for the schema; if access is denied, capture the error and ask the workspace administrator for the required catalog/schema permissions.
5. Run **Create and use a governed Volume** to create `playbook_files` and write/read `hello.txt`. In Catalog Explorer, navigate to the catalog, scratch schema, then `playbook_files`. Confirm the file appears; its path follows `/Volumes/<catalog>/<schema>/playbook_files/hello.txt`. Replace each angle-bracket item with the actual widget value; the brackets are notation, not part of the path.
6. Add a Markdown cell at the end with the table path, volume path, and why managed tables suit scratch or curated data.

## Check your work
The fully qualified schema is correct, the table is reported as managed, and the sample file can be read from the volume. Grant inspection may require additional permissions.

## Deliverable
Keep executed outputs and record the fully qualified table and volume paths plus one sentence on why managed tables are preferable for scratch/curated data.

## Cleanup
Keep the volume and its `hello.txt` file through topic 10. After the dependent labs and after saving your evidence, uncomment and run the notebook cleanup cell to drop only the assignment's `sample_features` table and `playbook_files` volume. Keep your personal scratch schema. Volume deletion requires appropriate privileges; if denied, ask its owner or administrator to remove it.

## Worked solution

Compare your work with the [solution notebook](solution.py).
