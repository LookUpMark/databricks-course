# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.
"""Fixtures for tests that connect to a Databricks workspace."""

import csv
import json
from pathlib import Path

import pytest
from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """Open a session using the configured Databricks profile and compute."""
    return DatabricksSession.builder.validateSession().getOrCreate()


@pytest.fixture()
def load_fixture(spark: SparkSession):
    """Load a JSON or CSV file from the repository's fixtures folder."""

    def _loader(filename: str):
        path = Path(__file__).resolve().parents[2] / "fixtures" / filename
        if path.suffix.lower() == ".json":
            return spark.createDataFrame(json.loads(path.read_text()))
        if path.suffix.lower() == ".csv":
            with path.open(newline="") as file:
                return spark.createDataFrame(list(csv.DictReader(file)))
        raise ValueError(f"Unsupported fixture type: {filename}")

    return _loader
