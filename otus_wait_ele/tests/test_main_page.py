from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page_elements(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 10)

    from selenium.common.exceptions import TimeoutException

    def test_main_page_elements(browser):
        browser.get(browser.base_url)
        wait = WebDriverWait(browser, 10)

        try:
            wait.until(EC.visibility_of_element_located((By.ID, "logo")))
        except TimeoutException:
            print("❌ Logo not found")

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "search")))
        except TimeoutException:
            print("❌ Search not found")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
        except TimeoutException:
            print("❌ My Account link not found")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-default.btn-lg")))
        except TimeoutException:
            print("❌ That big button not found")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart button")))
        except TimeoutException:
            print("❌ Cart button not found")
            raise AssertionError("❌ Cart button not found")

