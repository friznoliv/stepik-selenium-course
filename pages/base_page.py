from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def click(self, locator):
        WebDriverWait(self.browser, 8).until(ec.element_to_be_clickable(locator)).click()

    def text(self, locator):
        return WebDriverWait(self.browser, 8).until(ec.visibility_of_element_located(locator)).text

    def is_element_present(self, locator):
        return bool(self.browser.find_elements(*locator))

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.click(BasePageLocators.LOGIN_LINK)

    def go_to_basket_page(self):
        self.click(BasePageLocators.BASKET_LINK)

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is missing"

    def should_be_authorized_user(self):
        try:
            WebDriverWait(self.browser, 12).until(ec.presence_of_element_located(BasePageLocators.USER_ICON))
        except TimeoutException:
            raise AssertionError(f"Signed-in user icon is missing at {self.browser.current_url}") from None
