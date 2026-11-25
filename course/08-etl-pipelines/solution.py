# Databricks notebook source
# Assignment 08 - ETL Pipelines (medallion architecture).
# Simulates bronze -> silver -> gold on small JSON data, exercising Delta
# features: MERGE, time travel, table properties.

# COMMAND ----------
# MAGIC %md
# MAGIC # Assignment 08 — ETL Pipelines
# MAGIC
# MAGIC **Goal**: build a mini medallion pipeline and use Delta's core features.

# COMMAND ----------
import re

dbutils.widgets.text("catalog", defaultValue="")
dbutils.widgets.text("schema", defaultValue="")
catalog = dbutils.widgets.get("catalog").strip()
schema = dbutils.widgets.get("schema").strip()
identifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
if not catalog or not schema:
    raise ValueError("Set catalog and schema widgets to your pre-created writable Unity Catalog schema.")
if not identifier.fullmatch(catalog) or not identifier.fullmatch(schema):
    raise ValueError("catalog and schema must be simple Unity Catalog identifiers (letters, digits, underscores).")
scratch = f"`{catalog}`.`{schema}`"

# COMMAND ----------
# DBTITLE 1,Exercise 1 — bronze: raw data as it lands
# COMMAND ----------
import json
from pyspark.sql import Window, functions as F

raw_records = [
    {"event_id": "e1", "id": "c1", "name": "  Alice ", "amount": "100.5", "ts": "2026-01-01T10:00:00"},
    {"event_id": "e2", "id": "c2", "name": "Bob", "amount": "200.0", "ts": "2026-01-02T11:00:00"},
    {"event_id": "e3", "id": "c1", "name": "Alice", "amount": "110.0", "ts": "2026-01-03T09:30:00"},
    {"event_id": "e4", "id": None, "name": "bad", "amount": "x", "ts": "not-a-date"},
]
bronze_path = f"{scratch}.bronze_events"
source = spark.createDataFrame([(json.dumps(row),) for row in raw_records], "raw STRING")
if not spark.catalog.tableExists(bronze_path):
    spark.createDataFrame([], "raw STRING").write.format("delta").saveAsTable(bronze_path)
bronze_version = spark.sql(f"DESCRIBE HISTORY {bronze_path}").collect()[0]["version"]
incoming = source.select(F.from_json("raw", "event_id STRING, id STRING, name STRING, amount STRING, ts STRING").alias("j")).select("j.*")
incoming.createOrReplaceTempView("incoming_events")
spark.sql(f"""
MERGE INTO {bronze_path} AS target
USING (SELECT to_json(named_struct('event_id', event_id, 'id', id, 'name', name, 'amount', amount, 'ts', ts)) AS raw FROM incoming_events) AS source
ON get_json_object(target.raw, '$.event_id') = get_json_object(source.raw, '$.event_id')
WHEN MATCHED THEN UPDATE SET target.raw = source.raw
WHEN NOT MATCHED THEN INSERT (raw) VALUES (source.raw)
""")
print(f"Bronze rows: {spark.table(bronze_path).count()}")
spark.table(bronze_path).show(truncate=False)

# COMMAND ----------
# DBTITLE 1,Exercise 2 — silver: clean, dedupe, type
# COMMAND ----------
silver = (
    spark.table(bronze_path)
    .select(F.from_json("raw", "event_id STRING, id STRING, name STRING, amount STRING, ts STRING").alias("j"))
    .select("j.*")
    .withColumn("amount", F.expr("try_cast(amount AS DOUBLE)"))
    .withColumn("ts", F.expr("try_cast(ts AS TIMESTAMP)"))
    .filter(F.col("id").isNotNull() & F.col("amount").isNotNull())
    .withColumn("name", F.trim("name"))
    .filter(F.col("ts").isNotNull())
    .withColumn("rank", F.row_number().over(Window.partitionBy("id").orderBy(F.col("ts").desc(), F.col("event_id").desc())))
    .filter(F.col("rank") == 1)
    .drop("rank")
)
silver_df = silver  # keep for the MERGE below
silver_df.write.format("delta").mode("overwrite").saveAsTable(f"{scratch}.silver_events")
print(f"Silver rows: {silver_df.count()}")
spark.table(f"{scratch}.silver_events").show(truncate=False)

# COMMAND ----------
# DBTITLE 1,Exercise 3 — gold: MERGE into aggregate
# COMMAND ----------
totals = silver_df.groupBy("id").agg(F.sum("amount").alias("total_amount"))
gold = f"{scratch}.gold_customer_totals"
spark.sql(f"""
CREATE TABLE IF NOT EXISTS {gold} (id STRING, total_amount DOUBLE)
USING DELTA
""")

totals.createOrReplaceTempView("totals")
spark.sql(f"""
MERGE INTO {gold} g USING totals t ON g.id = t.id
WHEN MATCHED THEN UPDATE SET g.total_amount = t.total_amount
WHEN NOT MATCHED THEN INSERT (id, total_amount) VALUES (t.id, t.total_amount)
""")
print(f"Gold rows: {spark.table(gold).count()}")
spark.table(gold).show(truncate=False)

# COMMAND ----------
# DBTITLE 1,Exercise 4 — time travel
# COMMAND ----------
print(f"Bronze version captured before this run's merge: {bronze_version}")
spark.sql(f"SELECT * FROM {bronze_path} VERSION AS OF {bronze_version}").show(truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Exercise 5 (documented) — production bronze with Auto Loader
# MAGIC
# MAGIC Replace the simulated append with `spark.readStream.format("cloudFiles")`,
# MAGIC schema inference/evolution, and a **checkpoint location** per pipeline
# MAGIC (e.g. `/Volumes/{catalog}/{schema}/course_files/checkpoints/bronze_events`).
# MAGIC A checkpoint stores offsets and state for recovery; it does not by itself guarantee end-to-end exactly-once behavior. Keep a durable, unique checkpoint outside the driver local filesystem, for example a Unity Catalog volume path. Keep Auto Loader schema state under a separate durable schemaLocation such as `/Volumes/{catalog}/{schema}/course_files/schemas/bronze_events`. Create the `course_files` volume first and grant the pipeline identity the required volume permissions. Configure source and sink idempotently, and do not delete the checkpoint to "reset" a stream without understanding replay effects.
# MAGIC
# MAGIC ## Deliverable
# MAGIC
# MAGIC Add a markdown cell: the three table names, row counts, and where the
# MAGIC checkpoint would live.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Worked deliverable (example)
# MAGIC
# MAGIC The notebook prints live row counts for `<catalog>.<schema>.bronze_events`, `silver_events`, and `gold_customer_totals`; use those values from your run. The deterministic source event IDs and MERGE make reruns idempotent: expected counts are 4 bronze raw events, 2 valid unique customers in silver, and 2 customer totals in gold.
# MAGIC
# MAGIC Capture the Delta version before modifying a table, then query `VERSION AS OF` that recorded version; `DESCRIBE HISTORY` after a write returns the new latest version and is not a before/after comparison. Auto Loader production pattern: persist `cloudFiles.schemaLocation` and `checkpointLocation` in distinct durable Unity Catalog volume paths, unique to the stream. Checkpoints retain source offsets/state and support recovery; exactly-once outcome depends on the source/sink and idempotent writes.
# MAGIC
# MAGIC Cleanup: remove only these three assignment tables if you own them and have saved any desired history; dropping a table also removes its accessible history.
