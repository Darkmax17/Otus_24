from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_category_page_elements(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 10)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-thumb")))
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
