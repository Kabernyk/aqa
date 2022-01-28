from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebDriverListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((by, value)))


class WebDriver(EventFiringWebDriver):

    def wait_till_element_is_displayed(self, locator, timeout: int = 4):
        wait = WebDriverWait(self._driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
