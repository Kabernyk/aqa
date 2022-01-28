from selenium.webdriver.common.by import By

from page_object.modals.login_modal import LoginModal
from page_object.modals.register_modal import RegisterModal
from page_object.pages.base_page import BasePage
from helpers.logger import log


class HomePage(BasePage):
    _REGISTER_LINK = By.ID, "register"
    _LOGIN_LINK = By.ID, "login"
    _LOGGED_USER_TEXT = By.CSS_SELECTOR, "#howdy a"
    _ACCOUNT_TAB = By.ID, "tabAccount"
    _LOGIN_ERROR = By.CSS_SELECTOR, "#login-message div"

    def click_register_link(self):
        log.info("Click on register link")
        self._driver.find_element(*self._REGISTER_LINK).click()
        return RegisterModal(self._driver)

    def click_login_link(self):
        log.info("Click on login link")
        self._driver.find_element(*self._LOGIN_LINK).click()
        return LoginModal(self._driver)

    def get_logged_user_text(self):
        log.info("Get logged user text from home page")
        return self._driver.find_element(*self._LOGGED_USER_TEXT).text

    def is_account_tab_displayed(self):
        log.info("Is ACCOUNT tab displayed")
        return self._driver.wait_till_element_is_displayed(self._ACCOUNT_TAB)

    def is_sign_in_error_displayed(self):
        log.info("Is validation message displayed")
        return self._driver.find_element(*self._LOGIN_ERROR).text
