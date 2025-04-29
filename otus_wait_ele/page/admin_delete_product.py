from selenium.webdriver.common.by import By
from otus_wait_ele.page.base_page import BasePage

class AdminLoginPage(BasePage):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
