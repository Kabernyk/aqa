import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from helpers.web_driver.web_driver import WebDriver
from helpers.web_driver.web_driver import WebDriverListener


@pytest.fixture()
def driver():
    # before test
    driver_path = ChromeDriverManager().install()
    service = Service(executable_path=driver_path)
    _driver = Chrome(service=service)
    ef_driver = WebDriver(_driver, WebDriverListener())
    ef_driver.get("http://test-automation-course.dev.pro")
    yield ef_driver
    # after test
    ef_driver.quit()


@pytest.fixture()
def hello():
    print("Before test")
    yield
    print("After test")
