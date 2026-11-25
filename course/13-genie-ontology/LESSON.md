# Assignment 13 — Genie Ontology

Worked example: [solution notebook](solution.py).

## Before you start
Read the official [Genie overview](https://docs.databricks.com/aws/en/genie/), [Genie One](https://docs.databricks.com/aws/en/genie-one), and [Genie Code](https://docs.databricks.com/aws/en/genie-code) documentation. Run the notebook inventory and comment-verification cells using your personal schema from Assignment 02. The notebook reads the synthetic `orders` table from topic 03 and does not establish production quality or certification.

## Walkthrough
1. In Catalog Explorer, open the catalog and personal schema from the notebook widgets. Inspect `orders` and its comments.
2. Observe any certification label/status; do not certify this synthetic scratch table. Record if a control is unavailable.
3. Open Genie One from workspace navigation. Ask a question about `orders` only if the table is discoverable to your identity. Review the answer and any generated SQL/citations that the UI displays; record when a feature is unavailable.
4. Inspect Genie Code separately in a notebook or SQL editor. Ask it to explain the `orders` definition or draft a query. Review any generated code before running it. Genie Code is a coding/data assistant; Genie One is the simplified data interaction interface.
5. Compare only what you directly observed. Genie One and Genie Code search the same Genie Ontology: modeled knowledge is governed context you define through Unity Catalog semantics (for example metric views, domains, Pages, certification); learned knowledge is snippets extracted from assets and usage. What context is surfaced or usable can still vary by product surface, feature, permissions, and workspace configuration. Record a real discrepancy if one appears; otherwise mark your conflict as hypothetical. Do not assume a table comment alone is modeled ontology context.
6. Do not certify the synthetic scratch table. Explain that its generated sample rows are not quality-reviewed, authoritative business data.

## Check your work
The notebook inventory is complete. Your notes distinguish inspected Genie One output from Genie Code assistance, and document unavailable UI features without treating their absence as a failure.

## Deliverable
Record the Genie One answer/SQL review, the separate Genie Code observation, a real or clearly hypothetical discrepancy, and why synthetic scratch data must not be certified.
