from urllib.parse import urlparse

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert "login" in urlparse(self.browser.current_url).path, "Login page URL is missing login"
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is missing"
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), "Registration form is missing"

    def register_new_user(self, email, password):
        fields = (
            (LoginPageLocators.EMAIL, email),
            (LoginPageLocators.PASSWORD, password),
            (LoginPageLocators.CONFIRM_PASSWORD, password),
        )
        for locator, value in fields:
            self.browser.find_element(*locator).send_keys(value)
        self.click(LoginPageLocators.REGISTER)
