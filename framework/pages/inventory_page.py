from selenium.webdriver.common.by import By
from typing import List


class InventoryPage:
    """Page object for the Sauce Demo inventory page.

    Products are represented by elements with class `inventory_item` and the
    product name is in an element with class `inventory_item_name`.
    """

    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def product_names(self) -> List[str]:
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [el.text.strip() for el in items]

    def has_product(self, name: str) -> bool:
        return any(name == n for n in self.product_names())
