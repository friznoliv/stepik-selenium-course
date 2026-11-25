from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(BasketPageLocators.ITEMS), "Basket has product rows"
        assert "empty" in self.text(BasketPageLocators.EMPTY_NOTICE).lower(), "Empty basket notice is missing"
