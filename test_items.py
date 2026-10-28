"""Check that a product can be added to the basket in any interface language."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_product_page_has_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    buttons = WebDriverWait(browser, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket"))
    )
    assert len(buttons) == 1, "Expected one Add to basket button on the product page"
    assert buttons[0].is_displayed(), "Add to basket button is hidden"
