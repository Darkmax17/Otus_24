from selenium.webdriver.common.by import By

class AdminProductPage:
    def __init__(self, driver):
        self.driver = driver

    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    DATA_TAB = (By.LINK_TEXT, "Data")
    MODEL = (By.ID, "input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")

    def open_add_product_form(self):
        self.driver.find_element(*self.ADD_NEW_BUTTON).click()

    def fill_product_form(self, name, meta, model):
        self.driver.find_element(*self.PRODUCT_NAME).send_keys(name)
        self.driver.find_element(*self.META_TAG_TITLE).send_keys(meta)
        self.driver.find_element(*self.DATA_TAB).click()
        self.driver.find_element(*self.MODEL).send_keys(model)

    def save_product(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()
