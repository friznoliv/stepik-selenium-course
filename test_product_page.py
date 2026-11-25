from uuid import uuid4

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


SHOP = "https://selenium1py.pythonanywhere.com"
BOOK = f"{SHOP}/catalogue/coders-at-work_207/"
HANDBOOK = f"{SHOP}/catalogue/the-shellcoders-handbook_209/"


def add_and_check(page, promo=False, expect_code=False):
    page.open()
    name, price = page.name(), page.price()
    page.add_to_basket()
    if promo:
        page.solve_promo_quiz(expect_code=expect_code)
    page.should_confirm_product(name, price)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    add_and_check(ProductPage(browser, BOOK))


@pytest.mark.parametrize("url", [f"{HANDBOOK}?promo=newYear", f"{BOOK}?promo=newYear2019"])
def test_guest_can_add_product_with_new_year_promo(browser, url):
    add_and_check(ProductPage(browser, url), promo=True, expect_code=True)


@pytest.mark.parametrize(
    "offer",
    [
        pytest.param(
            7,
            marks=pytest.mark.xfail(raises=AssertionError, reason="Offer 7 changes the product name", strict=True),
        )
        if offer == 7
        else offer
        for offer in range(10)
    ],
)
def test_guest_can_add_product_with_numbered_promo(browser, offer):
    add_and_check(ProductPage(browser, f"{BOOK}?promo=offer{offer}"), promo=True)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, BOOK)
    page.open()
    page.go_to_basket_page()
    BasketPage(browser, browser.current_url).should_be_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, BOOK)
    page.open()
    page.go_to_login_page()
    LoginPage(browser, browser.current_url).should_be_login_page()


@pytest.mark.xfail(raises=AssertionError, reason="Adding a product shows a success message", strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BOOK)
    page.open()
    page.add_to_basket()
    page.should_not_show_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, BOOK)
    page.open()
    page.should_not_show_success_message()


@pytest.mark.xfail(raises=AssertionError, reason="The storefront keeps the success message visible", strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BOOK)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def register_user(self, browser):
        login = LoginPage(browser, f"{SHOP}/accounts/login/")
        login.open()
        login.register_new_user(f"stepik-{uuid4().hex}@example.com", f"Stepik!{uuid4().hex}")
        login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, BOOK)
        page.open()
        page.should_not_show_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        add_and_check(ProductPage(browser, BOOK))
