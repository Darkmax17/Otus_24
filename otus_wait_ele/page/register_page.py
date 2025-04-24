import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from otus_wait_ele.page.base_page import BasePage  # Абсолютный импорт — стабильнее

logger = logging.getLogger(__name__)

class RegisterPage(BasePage):
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM = (By.ID, "input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#content h1")

    @allure.step("Открываем страницу регистрации по адресу: {url}")
    def open(self, url="http://localhost/index.php?route=account/register"):
        logger.info(f"Opening register page: {url}")
        self.driver.get(url)

    @allure.step("Заполняем имя: {firstname}")
    def set_firstname(self, firstname):
        self.input_text(self.FIRSTNAME, firstname)

    @allure.step("Заполняем фамилию: {lastname}")
    def set_lastname(self, lastname):
        self.input_text(self.LASTNAME, lastname)

    @allure.step("Вводим email: {email}")
    def set_email(self, email):
        self.input_text(self.EMAIL, email)

    @allure.step("Вводим телефон: {telephone}")
    def set_telephone(self, telephone):
        self.input_text(self.TELEPHONE, telephone)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        self.input_text(self.PASSWORD, password)

    @allure.step("Подтверждаем пароль")
    def confirm_password(self, password):
        self.input_text(self.CONFIRM, password)

    @allure.step("Ставим галочку на согласие с политикой конфиденциальности")
    def accept_privacy_policy(self):
        self.click(self.PRIVACY_POLICY_CHECKBOX)

    @allure.step("Нажимаем кнопку 'Continue'")
    def submit_form(self):
        self.click(self.CONTINUE_BUTTON)

    @allure.step("Проверяем заголовок успешной регистрации")
    def get_success_title(self):
        return self.get_text(self.SUCCESS_TITLE)
