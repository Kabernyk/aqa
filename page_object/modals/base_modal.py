from selenium.webdriver.remote.webdriver import WebDriver


class BaseModal:
    def __init__(self, driver: WebDriver):
        self._driver = driver
