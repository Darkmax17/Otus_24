import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class AdminProductPage(BasePage):
    CATALOG_MENU = (By.ID, "menu-catalog")
    PRODUCTS_LINK = (By.LINK_TEXT, "Products")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    PRODUCT_CHECKBOXES = (By.NAME, "selected[]")
    PRODUCT_NAME_INPUT = (By.ID, "input-name1")
    META_TAG_INPUT = (By.ID, "input-meta-title1")
    DATA_TAB = (By.LINK_TEXT, "Data")
    MODEL_INPUT = (By.ID, "input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    @allure.step("Переход к списку товаров")
    def open_products_page(self):
        self.click(self.CATALOG_MENU)
        self.click(self.PRODUCTS_LINK)

    @allure.step("Добавление нового товара: '{name}'")
    def add_product(self, name, meta, model):
        self.click(self.ADD_NEW_BUTTON)
        self.input_text(self.PRODUCT_NAME_INPUT, name)
        self.input_text(self.META_TAG_INPUT, meta)
        self.click(self.DATA_TAB)
        self.input_text(self.MODEL_INPUT, model)
        self.click(self.SAVE_BUTTON)

    @allure.step("Удаление первого товара в списке")
    def delete_first_product(self):
        self.click(self.PRODUCT_CHECKBOXES)
        self.click(self.DELETE_BUTTON)
