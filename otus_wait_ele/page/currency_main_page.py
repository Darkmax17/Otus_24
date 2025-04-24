import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from otus_wait_ele.page.main_page import MainPage

def currency_switch_main_page(browser):
    page = MainPage(browser)
    page.open()

    wait = WebDriverWait(browser, 10)
    price_before = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text

    page.change_currency("EUR")

    price_after = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text
    assert price_before != price_after, "Цена не изменилась при смене валюты"
   @allure.step("Получаем список цен на странице")
    def get_all_prices(self):
        return self.driver.find_elements(*self.PRICES)