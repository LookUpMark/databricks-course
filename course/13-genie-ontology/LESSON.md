# Assignment 13 — Genie Ontology

Worked example: [solution notebook](solution.py).

## Before you start
Read the official [Genie overview](https://docs.databricks.com/aws/en/genie/), [Genie One](https://docs.databricks.com/aws/en/genie-one), and [Genie Code](https://docs.databricks.com/aws/en/genie-code) documentation. Open the [assignment notebook](databricks_notebook_source.py), set its `catalog` and `schema` widgets to your personal schema from Assignment 02, and run the inventory and comment-verification cells. The notebook reads the synthetic `orders` table from topic 03 and does not establish production quality or certification.

## Walkthrough
1. In Catalog Explorer, open the catalog and personal schema from the notebook widgets, select `orders`, and inspect its description and column comments. Confirm that the table and comments identify the data as synthetic and define paid orders as revenue.
2. Observe any certification label/status; do not certify this synthetic scratch table. Record if a control is unavailable.
3. Open Genie One from workspace navigation. If `orders` is discoverable to your identity, ask “What was the monthly paid revenue in EUR?” Compare the answer with the topic 03 sanity query: EUR 100 for January, EUR 250 for February, and EUR 120 for April 2026. Review any generated SQL/citations the UI displays; if SQL is shown, check that it filters to `status = 'paid'`. Record unavailable features rather than assuming the table comment was used.
4. In a separate notebook or SQL editor, open Genie Code and ask it to explain the `orders` definition or draft a query for monthly paid revenue. Review generated code before running it. Genie Code is a coding/data assistant; Genie One is the simplified data interaction interface. Record what each product actually showed.
5. Compare only what you directly observed. Genie One and Genie Code search the same Genie Ontology: modeled knowledge is governed context you define through Unity Catalog semantics (for example metric views, domains, Pages, certification); learned knowledge is snippets extracted from assets and usage. What context is surfaced or usable can still vary by product surface, feature, permissions, and workspace configuration. Record a real discrepancy if one appears; otherwise mark your conflict as hypothetical. Do not assume a table comment alone is modeled ontology context.
6. Do not certify the synthetic scratch table. Explain that its generated sample rows are not quality-reviewed, authoritative business data.

## Check your work
The notebook inventory is complete. Your notes distinguish inspected Genie One output from Genie Code assistance, and document unavailable UI features without treating their absence as a failure.

## Deliverable
Record the Genie One answer/SQL review, the separate Genie Code observation, a real or clearly hypothetical discrepancy, and why synthetic scratch data must not be certified.

## Cleanup

This is an inspection exercise and creates no new objects. Keep `orders` until all dependent labs are complete; use topic 03's cleanup instructions when it is safe to remove.
