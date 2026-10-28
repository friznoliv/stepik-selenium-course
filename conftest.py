"""Browser configuration for the Stepik language exercise."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="Browser interface language, e.g. es or fr")


@pytest.fixture
def browser(request):
    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
