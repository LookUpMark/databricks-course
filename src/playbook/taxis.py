# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.
"""Taxi data access functions.

Atomic data-access layer: each function does exactly one Spark operation and
takes its Spark session as a parameter, keeping the module testable without
the Databricks runtime.
"""

from pyspark.sql import DataFrame, SparkSession

# Fully-qualified source table read by this module.
NYC_TRIPS_TABLE = "samples.nyctaxi.trips"


def read_table(spark: SparkSession, table: str) -> DataFrame:
    """Read a Unity Catalog table as a DataFrame.

    Args:
        spark: Active Spark session.
        table: Fully-qualified table name, e.g. ``catalog.schema.table``.

    Returns:
        The table contents as a DataFrame.
    """
    return spark.read.table(table)


def find_all_taxis(spark: SparkSession) -> DataFrame:
    """Return all NYC taxi trips from the sample catalog.

    Args:
        spark: Active Spark session.

    Returns:
        DataFrame of the ``samples.nyctaxi.trips`` table.
    """
    return read_table(spark, NYC_TRIPS_TABLE)


def show_head(df: DataFrame, rows: int = 5) -> None:
    """Print the first rows of a DataFrame for quick inspection.

    Args:
        df: DataFrame to display.
        rows: Number of rows to print.
    """
    df.show(rows)
