from selenium.webdriver.common.by import By
from page_object.modals.base_modal import BaseModal
from helpers.logger import log


class LoginModal(BaseModal):
    _USERNAME_INPUT = By.ID, "username-modal"
    _PASSWORD_INPUT = By.ID, "password-modal"
    _LOGIN_BUTTON = By.CSS_SELECTOR, "#login-modal p button"
    _CLOSE_BUTTON = By.CSS_SELECTOR, "#login-modal  div  div  div.modal-header  button"

    def set_username(self, username: str = None):
        log.info(f"Set username '{username}' to login input field")
        self._driver.find_element(*self._USERNAME_INPUT).send_keys(username)

    def set_password(self, password: str = None):
        log.info("Set password to password input field")
        self._driver.find_element(*self._PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        log.info("Pres Login button")
        self._driver.find_element(*self._LOGIN_BUTTON).click()

    def click_close_login_button(self):
        log.info("Pres close button for login form")
        self._driver.find_element(*self._CLOSE_BUTTON).click()

    def login(self, username: str = None, password: str = None):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        self.click_close_login_button()





