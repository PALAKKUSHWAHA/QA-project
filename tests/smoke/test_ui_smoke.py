import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = os.getenv("TEST_BASE_URL", "")


def _make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_ui_smoke():
    """Basic Selenium smoke: open base URL and assert page loads.

    Skips when `TEST_BASE_URL` is not configured or when the webdriver cannot be
    started in the current environment (keeps CI stable for runners without a
    browser binary)."""
    if not BASE_URL:
        pytest.skip("TEST_BASE_URL not set — UI smoke skipped")

    try:
        driver = _make_driver()
    except Exception as e:
        pytest.skip(f"WebDriver not available in this environment: {e}")

    try:
        driver.get(BASE_URL)
        assert driver.current_url.startswith("http"), "Loaded URL is not HTTP(S)"
    finally:
        driver.quit()
