import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from framework.pages.login_page import LoginPage

BASE_URL = os.getenv("TEST_BASE_URL", "")
USERNAME = os.getenv("TEST_USERNAME", "")
PASSWORD = os.getenv("TEST_PASSWORD", "")


def _make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_login_smoke():
    """Login smoke test using the `LoginPage` page object.

    Skips when required environment variables are not provided or when a
    WebDriver cannot be started in the current environment.
    """
    if not (BASE_URL and USERNAME and PASSWORD):
        pytest.skip("TEST_BASE_URL/TEST_USERNAME/TEST_PASSWORD not set — login smoke skipped")

    try:
        driver = _make_driver()
    except Exception as e:
        pytest.skip(f"WebDriver not available in this environment: {e}")

    try:
        page = LoginPage(driver, BASE_URL)
        page.open('/')
        page.login(USERNAME, PASSWORD)
        driver.implicitly_wait(5)
        assert page.is_logged_in(), "Login did not result in expected logged-in state"
    finally:
        driver.quit()
