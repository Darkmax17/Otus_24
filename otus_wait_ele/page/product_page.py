from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    ADD_TO_CART = (By.ID, "button-cart")

    def open(self, product_url):
        self.driver.get(product_url)

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()