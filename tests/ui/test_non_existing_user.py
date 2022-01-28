from configs import config
from helpers.fake_data import Fake
from page_object.pages.home_page import HomePage


def test_valid_user_login(driver):
    # Arrange
    username = Fake.text(self=Fake())
    password = config.SEED_PASSWORD  # Use the password from real user to test security
    # Act
    home_page = HomePage(driver)
    login_modal = home_page.click_login_link()
    login_modal.login(username, password)

    # Assert
    assert "Invalid login credentials" == home_page.is_sign_in_error_displayed(), \
        "Expected validation message"
    assert f"Logged in as {username} {username}" == home_page.get_logged_user_text(), \
        "User exist or critical error was detected"
