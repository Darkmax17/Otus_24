from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_currency_switch_category_page(browser):
    browser.get(browser.base_url + "/index.php?route=product/category&path=20")  # Категория "Desktops"
    wait = WebDriverWait(browser, 10)

    price_before = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text

    browser.find_element(By.CSS_SELECTOR, "#form-currency button").click()
    browser.find_element(By.NAME, "GBP").click()

    price_after = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text

    assert price_before != price_after, "Цена в категории не изменилась при смене валюты"