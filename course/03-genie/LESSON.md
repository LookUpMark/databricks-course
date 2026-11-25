# Assignment 03 — Genie Agents

## Before you start
Run the notebook cells first. They create a clearly labeled synthetic `orders` table in your personal scratch schema; the Genie Agent is created separately in the workspace UI. Set non-empty `catalog` and `schema` widgets. You need the Databricks SQL entitlement, `CAN USE` on a Pro or serverless SQL warehouse, `USE CATALOG`, `USE SCHEMA`, and `SELECT` on the data the agent queries. Creating `orders` requires `CREATE TABLE`. Replacing it also requires ownership or `MANAGE` on the table; run this only in your personal schema. When editing an existing Genie Agent, you need at least `CAN EDIT`. See [Genie Agent requirements](https://docs.databricks.com/aws/en/genie-agents/set-up).

## Walkthrough
1. In the notebook, run the table creation cell and the comment-verification cell. Confirm the table and column comments describe the business meaning, especially which orders count as revenue.
2. Run the sanity SQL cell and note the expected revenue result. This gives you a reference answer to compare with Genie.
3. In the workspace sidebar, click **Genie Agents → New**. Select the `orders` table in your lab schema and click **Create**. Genie Code opens with context suggestions; review them before accepting. To change sources later, use **Configure → Data**.
4. Under **Configure**, add two concise instructions, including the revenue definition. Use **Examples** to save the monthly revenue SQL from the notebook as an example query. Databricks calls parameterized examples and Unity Catalog SQL functions [trusted assets](https://docs.databricks.com/aws/en/genie-agents/tune-quality/); this lab uses an ordinary example query.
5. Save the agent. Ask three natural-language questions about the sample data. For each response, open the generated SQL and compare it with the expected semantics and notebook result.
6. Mark one incorrect or weak answer using the available feedback control. If no answer is wrong, flag the least clear answer and explain the correction you would make.
7. Add a final Markdown cell recording the agent name, questions, SQL correctness, and an instruction you added or refined.

## Check your work
The agent uses the intended schema/table, instructions and the example query are saved, and you reviewed the SQL for all three questions.

## Deliverable
Keep notebook outputs and record the agent name, three questions, whether Genie generated correct SQL, and one instruction added after review.

## Cleanup
Keep the agent through topic 04 and the `orders` table through topics 05, 07 and 13. Then delete the Genie Agent from its **⋮** menu if you no longer need it and uncomment the notebook cleanup cell to drop the assignment's `orders` table. Keep your schema. Deleting the agent/table requires appropriate ownership or privileges.

## Worked solution

Compare your work with the [solution notebook](solution.py).
