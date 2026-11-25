from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def test_file_upload(browser, tmp_path):
    attachment = tmp_path / "stepik_upload.txt"
    attachment.write_text("Stepik Selenium file upload exercise\n", encoding="utf-8")
    browser.get("https://suninjuly.github.io/file_input.html")

    for name, value in {
        "firstname": "Selenium",
        "lastname": "Student",
        "email": "student@example.com",
    }.items():
        browser.find_element(By.NAME, name).send_keys(value)

    browser.find_element(By.ID, "file").send_keys(str(attachment))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    result = WebDriverWait(browser, 8).until(ec.alert_is_present())
    print(result.text)
    result.accept()
