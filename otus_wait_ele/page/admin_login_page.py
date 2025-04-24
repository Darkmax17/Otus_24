import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class AdminLoginPage(BasePage):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    @allure.step("Авторизация в админке с пользователем '{username}'")
    def login(self, username, password):
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
