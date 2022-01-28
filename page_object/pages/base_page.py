from conftest import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver) -> object:
        self._driver = driver
