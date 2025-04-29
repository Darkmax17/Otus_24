from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register_page_elements(browser):
    browser.get(f"{browser.base_url}/index.php?route=account/register")
    wait = WebDriverWait(browser, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.NAME, "agree")))