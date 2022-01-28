
from configs import config
from page_object.pages.home_page import HomePage


def test_valid_user_login(driver):
    # Arrange
    username = config.SEED_USERNAME
    password = config.SEED_PASSWORD
    firstname = config.SEED_FIRSTNAME
    lastname = config.SEED_LASTNAME
    # Act
    home_page = HomePage(driver)
    login_modal = home_page.click_login_link()
    login_modal.login(username, password)

    # Assert
    assert f"Logged in as {firstname} {lastname}" == home_page.get_logged_user_text(), \
        "Username is not displayed after sign in"
    assert home_page.is_account_tab_displayed(), "Account tab is not displayed after sign in"
