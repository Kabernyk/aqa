from selenium.webdriver.common.by import By
from page_object.modals.base_modal import BaseModal
from helpers.logger import log
from helpers.fake_data import Fake


class RegisterModal(BaseModal, Fake):
    _REGISTER_USERNAME = By.ID, "register-username-modal"
    _FIRST_NAME = By.ID, "register-first-modal"
    _LAST_NAME = By.ID, "register-last-modal"
    _EMAIL = By.ID, "register-email-modal"
    _REGISTER_PASSWORD = By.ID, "register-password-modal"
    _REGISTER_BUTTON = By.CSS_SELECTOR, "#register-modal p button"

    def set_register_username(self, register_name: str = None):
        log.info(f"Set username '{register_name}' to username register input field")
        self._driver.find_element(*self._REGISTER_USERNAME).send_keys(register_name)

    def set_first_name(self, first_name: str = None):
        log.info(f"Set firstname '{first_name}' to register input field")
        self._driver.find_element(*self._FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name: str = None):
        log.info(f"Set lastname '{last_name}' to register input field")
        self._driver.find_element(*self._LAST_NAME).send_keys(last_name)

    def set_email(self, email: str = None):
        log.info(f"Set email '{email}' to register input field")
        self._driver.find_element(*self._EMAIL).send_keys(email)

    def set_register_password(self, register_password: str = None):
        log.info(f"Set password '{register_password}' to register input field")
        self._driver.find_element(*self._REGISTER_PASSWORD).send_keys(register_password)

    def click_register_button(self):
        log.info("Pres Register button")
        self._driver.find_element(*self._REGISTER_BUTTON).click()

    def valid_register(self, register_username: str = None, first_name: str = None, last_name: str = None,
                       email: str = None,
                       register_password: str = None):
        self.set_register_username(register_username)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_register_password(register_password)
        self.click_register_button()

    def invalid_register(self, register_username: str = None, first_name: str = None, last_name: str = None,
                         register_password: str = None):
        self.set_register_username(register_username)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_register_password(register_password)
        self.click_register_button()
