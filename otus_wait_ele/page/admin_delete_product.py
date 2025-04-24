import allure
from selenium.webdriver.common.by import By

class AdminDeleteProductPage:
    def __init__(self, driver):
        self.driver = driver

    CHECKBOX = (By.NAME, "selected[]")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")

    @allure.step("Выделяем продукт для удаления")
    def select_product_checkbox(self):
        self.driver.find_element(*self.CHECKBOX).click()

    @allure.step("Нажимаем кнопку удаления продукта")
    def click_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()

    @allure.step("Подтверждаем алерт удаления")
    def accept_alert(self):
        self.driver.switch_to.alert.accept()
