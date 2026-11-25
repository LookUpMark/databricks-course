# Adapted from the Databricks default-python template. See THIRD_PARTY_NOTICES.md.
from playbook import taxis


def test_find_all_taxis(spark):
    results = taxis.find_all_taxis(spark)
    assert results.count() > 5
