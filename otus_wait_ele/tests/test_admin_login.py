from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_login(browser):
    browser.get(f"{browser.base_url}/admin")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "input-username"))).send_keys("admin")
    wait.until(EC.visibility_of_element_located((By.ID, "input-password"))).send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-nav .dropdown"))
