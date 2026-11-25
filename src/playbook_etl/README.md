# Lakeflow pipeline code

These Python transformations are used by the `refresh_pipeline` task in [sample_job](../../resources/sample_job.job.yml). It is part of [topic 09](../../course/09-lakeflow-jobs/LESSON.md). The [pipeline YAML](../../resources/playbook_etl.pipeline.yml) sends its outputs to the learner's configured catalog and schema.

| Transformation | Materialized view |
|---|---|
| [sample_trips_playbook.py](transformations/sample_trips_playbook.py) | `sample_trips_playbook` reads the NYC taxi sample data. |
| [sample_zones_playbook.py](transformations/sample_zones_playbook.py) | `sample_zones_playbook` sums fares by pickup ZIP. |

Lakeflow tracks this dependency automatically. Open **Jobs & Pipelines**, select your development pipeline, and inspect the graph and most recent update. The [Lakeflow Python reference](https://docs.databricks.com/aws/en/ldp/developer/python-ref) covers declarative transformations.
