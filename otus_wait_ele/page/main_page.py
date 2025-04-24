import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, ".btn-group button.dropdown-toggle")
    CURRENCY_OPTIONS = (By.CSS_SELECTOR, ".btn-group.open .dropdown-menu button")

    @allure.step("Открытие главной страницы OpenCart")
    def open(self, url="http://localhost/"):
        self.driver.get(url)

    @allure.step("Переключение валюты на: {currency_code}")
    def change_currency(self, currency_code):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.CURRENCY_DROPDOWN)).click()
        currency_buttons = wait.until(EC.presence_of_all_elements_located(self.CURRENCY_OPTIONS))

        for button in currency_buttons:
            if currency_code.lower() in button.get_attribute("name").lower():
                button.click()
                return True
        raise Exception(f"Currency '{currency_code}' not found in dropdown")
