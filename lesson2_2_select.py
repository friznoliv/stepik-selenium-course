"""Stepik 575, module 2.2: select the sum of the displayed numbers.

Install Selenium and Google Chrome, then run:
    python lesson2_2_select.py
The optional argument selects the second version of the form:
    python lesson2_2_select.py selects2
"""

import re
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

page = sys.argv[1] if len(sys.argv) > 1 else "selects1"
if page not in ("selects1", "selects2"):
    raise ValueError("Expected selects1 or selects2")

browser = webdriver.Chrome()
try:
    browser.get(f"https://suninjuly.github.io/{page}.html")
    problem = browser.find_element(By.TAG_NAME, "h2").text
    numbers = [int(value) for value in re.findall(r"\d+", problem)]
    assert len(numbers) == 2, f"Unexpected problem: {problem}"
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_visible_text(
        str(sum(numbers))
    )
    browser.find_element(By.TAG_NAME, "button").click()
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    assert "Congrats" in alert.text, alert.text
    print(alert.text)
    alert.accept()
finally:
    browser.quit()
