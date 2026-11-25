# Assignment 03 — AI/BI Genie Spaces

## Before you start
Run the notebook cells first. They create a clearly labeled synthetic `orders` table in your personal scratch schema; the Genie space is created separately in the workspace UI. Set non-empty `catalog` and `schema` widgets. You need permission to use a SQL warehouse, create a Genie space, use the catalog/schema and create or replace the table. Replacing `orders` overwrites only that named table in your supplied schema.

## Walkthrough
1. In the notebook, run the table creation cell and the comment-verification cell. Confirm the table and column comments describe the business meaning, especially which orders count as revenue.
2. Run the sanity SQL cell and note the expected revenue result. This gives you a reference answer to compare with Genie.
3. In the left navigation click **AI/BI**, then **Genie**, and choose **Create space**. Select your personal scratch schema and add the `orders` table. You need permission to use the catalog/schema and access the table. If the schema is not listed, ask its owner to grant access.
4. In the space editor, add two concise instructions, including the revenue definition. Add a trusted query that computes revenue using the same definition as the notebook.
5. Save the space. Ask three natural-language questions about the sample data. For each response, open the generated SQL and compare it with the expected semantics and notebook result.
6. Mark one incorrect or weak answer using the available feedback control. If no answer is wrong, flag the least clear answer and explain the correction you would make.
7. Add a final Markdown cell recording the space name, questions, SQL correctness, and an instruction you added or refined.

## Check your work
The space uses the intended schema/table, instructions and trusted query are saved, and you reviewed the SQL for all three questions.

## Deliverable
Keep notebook outputs and record the space name, three questions, whether Genie generated correct SQL, and one instruction added after review.

## Cleanup
Keep the space through topic 04 and the `orders` table through topics 05, 07 and 13. Then delete the Genie space from its **⋮** menu if you no longer need it and uncomment the notebook cleanup cell to drop the assignment's `orders` table. Keep your schema. Deleting the space/table requires appropriate ownership or privileges.

## Worked solution

Compare your work with the [solution notebook](solution.py).
