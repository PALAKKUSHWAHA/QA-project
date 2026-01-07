import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from framework.pages.sauce_login_page import SauceLoginPage

# Defaults: use Sauce Demo public demo site and credentials when env not set
BASE_URL = os.getenv("TEST_BASE_URL", "https://www.saucedemo.com")
USERNAME = os.getenv("TEST_USERNAME", "standard_user")
PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")


def _make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_login_saucedemo():
    """Login smoke for Sauce Demo using explicit selectors.

    Skips when WebDriver cannot be started in the current environment.
    """
    try:
        driver = _make_driver()
    except Exception as e:
        pytest.skip(f"WebDriver not available in this environment: {e}")

    try:
        page = SauceLoginPage(driver, BASE_URL)
        page.open()
        page.login(USERNAME, PASSWORD)
        driver.implicitly_wait(3)
        assert page.is_logged_in(), "Sauce Demo login failed or inventory page not reached"
    finally:
        driver.quit()
