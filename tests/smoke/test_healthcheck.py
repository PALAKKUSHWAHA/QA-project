import os
import pytest
import requests

BASE_URL = os.getenv("TEST_BASE_URL", "")

def test_healthcheck():
    """Simple smoke test: requests /health when TEST_BASE_URL is set.

    If `TEST_BASE_URL` is not configured the test is skipped so the suite
    remains runnable as a placeholder.
    """
    if not BASE_URL:
        pytest.skip("TEST_BASE_URL not set — placeholder smoke test skipped")

    resp = requests.get(BASE_URL.rstrip('/') + '/health')
    assert resp.status_code == 200, f"Health endpoint returned {resp.status_code}"
