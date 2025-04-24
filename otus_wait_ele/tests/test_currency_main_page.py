from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_currency_switch_main_page(browser):
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 10)

    # Получим цену до смены валюты
    price_before = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text

    # Открываем валютный селектор и выбираем евро
    browser.find_element(By.CSS_SELECTOR, "#form-currency button").click()
    browser.find_element(By.NAME, "EUR").click()

    # Получим цену после смены валюты
    price_after = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text

    assert price_before != price_after, "Цена не изменилась при смене валюты"
