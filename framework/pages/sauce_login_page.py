from selenium.webdriver.common.by import By


class SauceLoginPage:
    """Page object for https://www.saucedemo.com/ (Sauce Demo).

    Selectors are explicit for the demo site:
    - username: id `user-name`
    - password: id `password`
    - login button: id `login-button`
    After successful login the app navigates to `/inventory.html`.
    """

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver, base_url: str = "https://www.saucedemo.com"):
        self.driver = driver
        self.base_url = base_url.rstrip('/')

    def open(self):
        self.driver.get(self.base_url + '/')

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def is_logged_in(self) -> bool:
        return '/inventory.html' in self.driver.current_url
