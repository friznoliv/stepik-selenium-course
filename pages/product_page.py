import math

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def name(self):
        return self.text(ProductPageLocators.PRODUCT_NAME)

    def price(self):
        return self.text(ProductPageLocators.PRODUCT_PRICE)

    def add_to_basket(self):
        self.click(ProductPageLocators.ADD_TO_BASKET)

    def solve_promo_quiz(self, expect_code=False):
        wait = WebDriverWait(self.browser, 8)
        prompt = wait.until(ec.alert_is_present())
        x = float(prompt.text.split()[2])
        prompt.send_keys(str(math.log(abs(12 * math.sin(x)))))
        prompt.accept()
        if expect_code:
            result = wait.until(ec.alert_is_present())
            print(f"{self.url} → {result.text}")
            result.accept()

    def should_confirm_product(self, expected_name, expected_price):
        added_name = self.text(ProductPageLocators.SUCCESS_NAME)
        basket_total = self.text(ProductPageLocators.BASKET_TOTAL)
        assert added_name == expected_name, f"Added product: {added_name!r}, expected: {expected_name!r}"
        assert basket_total == expected_price, f"Basket total: {basket_total!r}, expected: {expected_price!r}"

    def should_not_show_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.SUCCESS_NAME), "Unexpected success message"

    def success_message_should_disappear(self):
        WebDriverWait(self.browser, 8).until(ec.visibility_of_element_located(ProductPageLocators.SUCCESS_NAME))
        assert self.is_disappeared(ProductPageLocators.SUCCESS_NAME), "Success message stayed visible"
