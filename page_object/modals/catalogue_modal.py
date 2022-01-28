from selenium.webdriver.common.by import By
from page_object.modals.base_modal import BaseModal
from helpers.logger import log


class PaymentModal(BaseModal):
    _CARD_NUMBER = By.ID, "form-card-number"
    _CARD_EXPIRES = By.ID, 'form-expires'
    _CCV = By.ID, "form-ccv"
    _PAYMENT_UPDATE = By.CSS_SELECTOR, "#card-modal  div  div  div.modal-body  p  button"

    def set_card_number(self, card_number: str = None):
        log.info(f"Set card number '{card_number}' to payment change input field")
        self._driver.find_element(*self._CARD_NUMBER).send_keys(card_number)

    def set_card_expires(self, card_expires: str = None):
        log.info(f"Set card expires '{card_expires}'  to payment change input field")
        self._driver.find_element(*self._CARD_EXPIRES).send_keys(card_expires)

    def set_ccv(self, ccv: str = None):
        log.info(f"Set ccv '{ccv}' to payment change input field")
        self._driver.find_element(*self._CCV).send_keys(ccv)

    def click_payment_update_button(self):
        log.info("Pres Update button")
        self._driver.find_element(*self._PAYMENT_UPDATE).click()

    def payment_update(self, card_number: str = None, card_expires: str = None, ccv: str = None):
        self.set_card_number(card_number)
        self.set_card_expires(card_expires)
        self.set_ccv(ccv)
        self.click_payment_update_button()


class CatalogueModal(PaymentModal):
    _HOUSE_NUMBER = By.ID, "form-number"
    _STREET_NAME = By.ID, "form-street"
    _CITY = By.ID, "form-city"
    _POST_CODE = By.ID, "form-post-code"
    _COUNTRY = By.ID, "form-country"
    _SHIPPING_UPDATE = By.CSS_SELECTOR, "#form-address  p  button"

    def set_house_number(self, house_number: str = None):
        log.info(f"Set house number '{house_number}' to shipping change input field")
        self._driver.find_element(*self._HOUSE_NUMBER).send_keys(house_number)

    def set_street_name(self, street_name: str = None):
        log.info(f"Set street name '{street_name}' to shipping change input field")
        self._driver.find_element(*self._STREET_NAME).send_keys(street_name)

    def set_city(self, city: str = None):
        log.info(f"Set city '{city}' to shipping change input field")
        self._driver.find_element(*self._CITY).send_keys(city)

    def set_post_code(self, post_code: str = None):
        log.info(f"Set post code '{post_code}' to shipping change input field")
        self._driver.find_element(*self._POST_CODE).send_keys(post_code)

    def set_country(self, country: str = None):
        log.info(f"Set country '{country}' to shipping change input field")
        self._driver.find_element(*self._COUNTRY).send_keys(country)

    def click_update_button(self):
        log.info("Pres Register button")
        self._driver.find_element(*self._SHIPPING_UPDATE).click()

    def shipping_update(self, house_number: str = None, street_name: str = None, city: str = None,
                        post_code: str = None, country: str = None):
        self.set_house_number(house_number)
        self.set_street_name(street_name)
        self.set_city(city)
        self.set_post_code(post_code)
        self.set_country(country)
        self.click_update_button()


class OrderCheckout(CatalogueModal):
    _CHECKOUT_BUTTON = By.ID, "orderButton"

    def click_checkout_button(self):
        log.info("Click checkout button")
        self._driver.find_element(*self._CHECKOUT_BUTTON).click()
