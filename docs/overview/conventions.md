# Conventions

- Keep lab guides and code comments in English. Each numbered topic has a README, a lesson, an exercise notebook, and a worked solution.
- Use the `.py` Databricks notebook source format. Start with `# Databricks notebook source`, separate cells with `# COMMAND ----------`, and use `# MAGIC %md` for Markdown cells.
- Use widgets for job arguments and learner-specific notebook inputs. Make the schema explicit in any lab with writes, and use synthetic or public data in examples.
- Keep reusable Python logic in `src/playbook/`, with a focused module for each purpose. Accept Spark sessions and external clients as arguments where practical. Use Google-style docstrings and Loguru in the package.
- Keep domain YAML and its Pydantic validation under `src/playbook/config/`. See [bundle setup](../../README.md#run-the-bundle) for workspace configuration.
- Run `task test` for offline package tests and `task lint` for Ruff checks. The [test guide](../../tests/README.md) explains live integration separately.
- Write descriptive Conventional Commits such as `docs(course): clarify Unity Catalog setup`.
