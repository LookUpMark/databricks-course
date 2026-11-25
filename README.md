# Databricks Course

A hands-on course for engineers learning Databricks. The 14 labs start with notebooks and Unity Catalog, then cover analytics, MLflow, jobs, pipelines, agents, and apps. The repository also contains a working Declarative Automation Bundle (DAB) based on the Databricks `default-python` template.

**Start with the [course index](course/README.md)**. It lists the labs in order, the features each one uses, and the exercises that depend on earlier work.

## Choose how to work

| Path | What you need | Where to start |
|---|---|---|
| Workspace labs | A Databricks workspace, permission to create files in your user folder, and compute you can use | Add this repository as a Databricks Git folder, then open [01 — Workspace](course/01-workspace/README.md) |
| Bundle and CLI labs (09–10) | A local terminal, Git, Python 3.12, [uv](https://docs.astral.sh/uv/getting-started/installation/), Databricks CLI 1.21.0+, `jq` for topic 10, and access to serverless Jobs and Pipelines | Clone the repo, then follow [Run the bundle](#run-the-bundle) |
| Develop the bundle code | The local tools above. [Go Task](https://taskfile.dev/installation/) is optional | See [Local development](#local-development) and the [developer docs](docs/README.md) |

Use a workspace approved for learning. A [Databricks Free Edition workspace](https://docs.databricks.com/aws/en/getting-started/free-edition-limitations) can cover many labs, subject to feature availability, region, permissions, and quota. Genie and dashboards need access to a SQL warehouse. Model Serving, Lakebase, Agent Bricks, and Apps have their own requirements. Each lesson identifies those requirements and explains what to record if access is unavailable. Jobs, serving, and deployments can consume compute. Use the personal development resources described in the lesson and clean up any resources you create.

## Work through a lab

1. In Databricks, open **Workspace**, go to your user folder, and create a **Git folder** using `https://github.com/LookUpMark/databricks-course.git`. If your workspace restricts Git folders, download the topic's `.py` notebook source and use **Workspace → Import**. For labs involving a second notebook, import both into the same folder. See [Databricks Git folders](https://docs.databricks.com/aws/en/repos/).
2. Open a numbered topic under [course/](course/README.md) and read its `LESSON.md` for the prerequisites and exact sequence. Attach the type of compute required by the lesson. Open `databricks_notebook_source.py` in Databricks, complete the required widgets, and run the cells in order. Follow the steps in the UI or your local terminal when the lesson calls for them.
3. Finish the **Deliverable** listed in the lesson. Write your observations in a Markdown cell in your own workspace copy. Keep screenshots, scripts, and any personal notes in your workspace or a local ignored `deliverables/` folder. Redact workspace links, account details, and credentials before sharing results outside your team.
4. Compare your work with `solution.py` after attempting the exercise. It is a Databricks notebook with the completed code, expected output, and an example deliverable. An example involving clicks, permissions, URLs, or IDs illustrates what to record from your own run. Use a fresh notebook copy and the intended lab schema before running cells that create or replace sample data.

### Set up your Unity Catalog sandbox

Topic [02 — Unity Catalog](course/02-unity-catalog/LESSON.md) explains how to find a writable catalog and set up a **personal lab schema**. In a shared workspace give it a unique simple name, such as `course_yourname`, and use the same catalog and schema in subsequent lab widgets and bundle variables. The example names use letters, numbers, and underscores, starting with a letter or underscore. If you cannot create a schema, ask the workspace owner for a dedicated existing one. Check that you can create the tables, views, or volumes called for by each lesson.

Keep the topic 02 volume through topic 10 and the topic 03 `orders` table through topics 05, 07, and 13. The topic 03 Genie space is used by topic 04. Topic [08](course/08-etl-pipelines/LESSON.md) builds its own Medallion tables in the lab schema. Topic 09 uses the workspace's read-only `samples.nyctaxi.trips` data in addition to the lab schema. Check [the index](course/README.md) before deleting shared course objects.

## Run the bundle

Install the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install) and run these commands in your **local terminal**, from the cloned repository. Replace the example workspace URL, catalog, and schema with your own values. The schema must already exist before you deploy the bundle.

```bash
git clone https://github.com/LookUpMark/databricks-course.git
cd databricks-course

databricks --version
databricks auth login --host 'https://YOUR_WORKSPACE_HOST' --profile course
export DATABRICKS_CONFIG_PROFILE=course
databricks auth describe --profile course

export BUNDLE_VAR_catalog='your_writable_catalog'
export BUNDLE_VAR_schema='course_yourname'

uv python install 3.12
uv sync --locked --no-dev
databricks bundle validate --target dev
databricks bundle deploy --target dev
databricks bundle run sample_job --target dev
```

- **Authentication** uses the named CLI profile on your machine. `auth describe` lets you check the host with credentials masked. If you see a different workspace, inspect your active profile and any Databricks auth environment overrides before deploying.
- **Validate** checks bundle configuration and resolves resource references. To preview the uploaded files, use `databricks bundle sync --target dev --dry-run`.
- **Deploy** builds the `playbook` wheel with `uv`, uploads the job notebook and pipeline sources, and creates a personal development copy of the job and pipeline. The workspace puts it under your user folder's `.bundle/databricks_course/dev` path by default. The development resource names have a `[dev …]` prefix and the periodic trigger is paused.
- **Run** starts `sample_job` manually. Open the run URL in **Jobs & Pipelines** and open the task graph. After the notebook checks the schema and previews five rows, the wheel previews NYC taxi trips and the pipeline refreshes its two materialized views in parallel. [Topic 09](course/09-lakeflow-jobs/LESSON.md) explains each task, job parameter and check. [Topic 10](course/10-cli-mastery/LESSON.md) shows how to inspect the run from the terminal.
- **Clean up** with `databricks bundle destroy --target dev` when you have finished both labs. Check the target and confirmation prompt first. Check your personal UC schema separately for course tables, views, and volumes, and delete only the assets you created and no longer need.

If deployment fails, read the first error. Common checks are CLI version, the active profile, the two bundle variables, permission to write to the selected schema, serverless availability, and access to the sample taxi table. The [bundle walkthrough](docs/overview/pipelines.md) explains how each resource is wired.

## Repository map

| Path | Purpose |
|---|---|
| [course/](course/README.md) | The student-facing material. Each topic has a short `README.md`, `LESSON.md`, `databricks_notebook_source.py` for practising, and `solution.py` for checking your work. |
| [databricks.yml](databricks.yml) | Bundle entry point. Includes resource definitions, builds the Python wheel, selects paths to sync, declares the catalog/schema variables, and sets up `dev`. |
| [resources/](resources/README.md) | Deployable YAML definitions for `sample_job` and `playbook_etl`. These are part of the bundle lab. |
| [src/sample_notebook.py](src/sample_notebook.py) | First task of `sample_job`. Shows how job parameters arrive as widgets and checks the intended schema. |
| [src/playbook/](src/playbook/README.md) | Python package built as a wheel and called by the job. The `main` entry point uses `context.py` and the `config/` YAML/Pydantic loader, previews trips via `taxis.py`, and uses `utils/` for CLI parsing and logging. |
| [src/playbook_etl/](src/playbook_etl/README.md) | Lakeflow Spark Declarative Pipelines code. Its `transformations/` directory defines the taxi trips view and an aggregate by pickup ZIP. The sample job refreshes this pipeline. |
| [tests/](tests/README.md) | Developer tests for the Python package. `unit/` and `e2e/` work offline. `integration/` needs Databricks Connect and live compute. |
| [tasks/](tasks/README.md) | **Optional placeholder** for future task wrappers. The current course and bundle use no code from this folder. |
| [fixtures/](fixtures/README.md) | **Optional placeholder** for small synthetic test inputs. The current exercises use generated rows or Databricks sample data. |
| [docs/](docs/README.md) | Architecture, configuration, job/pipeline walkthroughs, and guides to individual Python modules. Read these when changing or extending the bundle. |
| [pyproject.toml](pyproject.toml), [uv.lock](uv.lock) | Python version, dependencies, wheel build and `main` entry point, and the pinned dependency resolution. |
| [Taskfile.yml](Taskfile.yml) | Optional shortcuts for local checks and bundle commands. Run `task --list` to see them. |
| [.gitignore](.gitignore) | Keeps generated files, local credentials, and personal lab outputs out of Git. |
| [LICENSE](LICENSE), [third-party notices](THIRD_PARTY_NOTICES.md) | MIT terms for original course material and attribution and license for material adapted from Databricks. |

## Local development

From the root:

```bash
uv sync --locked --dev
uv run pytest tests/unit tests/e2e
uv run ruff check src tasks tests
uv build --wheel
```

The notebooks use Databricks-provided globals such as `spark`, `dbutils`, and `display`, so open them in the workspace. The package and offline tests can be edited and run locally. Optional live integration tests are described in [tests/README.md](tests/README.md). The examples use Databricks notebook-source `.py` files. When changing a lab, update both notebook versions and the lesson together, and keep actual workspace IDs, output and credentials out of the repository.
