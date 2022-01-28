from selenium.webdriver.common.by import By
from page_object.pages.home_page import HomePage
from helpers.logger import log
from page_object.modals.catalogue_modal import CatalogueModal


class Catalogue(HomePage):
    _CATALOGUE_TAB = By.ID, "tabCatalogue"
    _SELECT_FILTER = By.CSS_SELECTOR, '#filters  div:nth-child(9)  label  input[type=checkbox]'
    _APPLY_FILTER = By.CSS_SELECTOR, '#filters-form  a'
    _ADD_ITEMS = By.CSS_SELECTOR, '#products  div  div  div.text  p.buttons  a.btn.btn-primary'
    _CART_ITEM = By.CSS_SELECTOR, '#basket-overview > a > i'
    _SHIPPING_CHANGE = By.CSS_SELECTOR, "#basket  div:nth-child(2)  div:nth-child(1)  div  div.box-header  p  a"
    _PAYMENT_CHANGE = By.CSS_SELECTOR, "#basket > div:nth-child(2)  div:nth-child(2)  div  div.box-header  p  a"
    _ORDER_TEXT = By.ID, 'address'

    def click_catalogue_tab(self):
        log.info("Click on the catalogue tab")
        self._driver.find_element(*self._CATALOGUE_TAB).click()
        log.info("Select product filter")
        self._driver.find_element(*self._SELECT_FILTER).click()
        log.info("Click on the filter apply button")
        self._driver.find_element(*self._APPLY_FILTER).click()
        log.info("Click on the filter apply button")
        self._driver.find_element(*self._ADD_ITEMS).click()
        return CatalogueModal(self._driver)

    def click_item_button(self):
        log.info("Click on the cart item button ")
        self._driver.find_element(*self._CART_ITEM).click()
        return CatalogueModal(self._driver)

    def click_shipping_change_button(self):
        log.info("Click on the Change shipping button")
        self._driver.find_element(*self._SHIPPING_CHANGE).click()
        return CatalogueModal(self._driver)

    def click_payment_change_button(self):
        log.info("Click on the Change payment button")
        self._driver.find_element(*self._PAYMENT_CHANGE).click()
        return CatalogueModal(self._driver)

    def is_order_displayed(self):
        log.info("Is SHIPPING text is displayed on a tab")
        return self._driver.find_element(self._ORDER_TEXT).text()
