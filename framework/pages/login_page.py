from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip('/')

        # common selectors used by many apps; _find_first will try them in order
        self.username_selectors = [
            (By.ID, 'username'),
            (By.NAME, 'username'),
            (By.CSS_SELECTOR, 'input[type="email"]'),
        ]
        self.password_selectors = [
            (By.ID, 'password'),
            (By.NAME, 'password'),
            (By.CSS_SELECTOR, 'input[type="password"]'),
        ]
        self.submit_selectors = [
            (By.ID, 'login'),
            (By.NAME, 'login'),
            (By.CSS_SELECTOR, 'button[type="submit"]'),
        ]
        self.logout_selectors = [
            (By.LINK_TEXT, 'Logout'),
            (By.XPATH, "//button[contains(.,'Logout') or contains(.,'Sign out')]")
        ]

    def open(self, path: str = '/') -> None:
        self.driver.get(self.base_url + path)

    def _find_first(self, selectors):
        for by, sel in selectors:
            try:
                elem = self.driver.find_element(by, sel)
                return elem
            except NoSuchElementException:
                continue
        raise NoSuchElementException(f'No selector matched among: {selectors}')

    def login(self, username: str, password: str) -> None:
        user = self._find_first(self.username_selectors)
        pwd = self._find_first(self.password_selectors)

        try:
            user.clear()
            user.send_keys(username)
        except Exception:
            pass

        try:
            pwd.clear()
            pwd.send_keys(password)
        except Exception:
            pass

        try:
            submit = self._find_first(self.submit_selectors)
            submit.click()
        except NoSuchElementException:
            try:
                pwd.submit()
            except Exception:
                pass

    def is_logged_in(self) -> bool:
        for by, sel in self.logout_selectors:
            try:
                if self.driver.find_element(by, sel):
                    return True
            except NoSuchElementException:
                continue
        return False
