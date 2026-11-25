# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.
from pyspark import pipelines as dp


@dp.materialized_view
def sample_trips_playbook():
    """Expose the sample NYC taxi trips as a materialized view.

    Returns:
        DataFrame: NYC taxi trips from the Unity Catalog sample dataset.
    """
    return spark.read.table("samples.nyctaxi.trips")
