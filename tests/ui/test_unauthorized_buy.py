from page_object.pages.catalogue_page import Catalogue
from helpers.fake_data import Fake


def test_shipping_update(driver):
    # Arrange
    house_number = Fake.house_number(Fake())
    street_name = Fake.street(Fake())
    city = Fake.city(Fake())
    post_code = Fake.post_code(Fake())
    country = Fake.country(Fake())
    credit_cart = Fake.credit_card(Fake())
    credit_cart_expire = Fake.credit_card_expire(Fake())
    credit_cart_cvv = Fake.credit_card_cvv(Fake())

    # Act
    catalogue = Catalogue(driver)
    catalogue.click_catalogue_tab()
    catalogue.click_item_button()
    catalogue_page = catalogue.click_shipping_change_button()
    catalogue_page.shipping_update(house_number, street_name, city, post_code, country)
    payment_page = catalogue.click_payment_change_button()
    payment_page.payment_update(credit_cart, credit_cart_expire, credit_cart_cvv)


