# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.
from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view
def sample_zones_playbook():
    """Aggregate the fares from the sample trips by pickup ZIP.

    Returns:
        DataFrame: Total fare per pickup ZIP.
    """
    return (
        spark.read.table("sample_trips_playbook")
        .groupBy("pickup_zip")
        .agg(F.sum("fare_amount").alias("total_fare"))
    )
