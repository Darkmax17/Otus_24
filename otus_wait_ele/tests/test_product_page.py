from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_page_elements(browser):
    browser.get(f"{browser.base_url}/index.php?route=product/product&product_id=40")
    wait = WebDriverWait(browser, 10)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-thumb")))
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "price")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image")))

