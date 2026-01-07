import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from framework.pages.sauce_login_page import SauceLoginPage
from framework.pages.inventory_page import InventoryPage


def _make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_inventory_contains_backpack():
    """Login to Sauce Demo and verify 'Sauce Labs Backpack' appears in inventory."""
    try:
        driver = _make_driver()
    except Exception as e:
        pytest.skip(f"WebDriver not available in this environment: {e}")

    try:
        login = SauceLoginPage(driver)
        login.open()
        login.login('standard_user', 'secret_sauce')

        inv = InventoryPage(driver)
        driver.implicitly_wait(3)
        assert inv.has_product('Sauce Labs Backpack'), 'Expected product not found in inventory'
    finally:
        driver.quit()
