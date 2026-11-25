"""Browser configuration shared by the course exercises."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", default="en", help="Preferred storefront language")
    parser.addoption("--headless", action="store_true", help="Run Chrome without a window")


@pytest.fixture
def browser(request):
    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    options.add_argument("--window-size=1440,1000")
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()
