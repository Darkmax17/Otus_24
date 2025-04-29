from selenium.webdriver.common.by import By

class AdminCatalogPage:
    def __init__(self, driver):
        self.driver = driver

    CATALOG_MENU = (By.ID, "menu-catalog")
    PRODUCTS_LINK = (By.XPATH, "//a[text()='Products']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    PRODUCT_CHECKBOXES = (By.CSS_SELECTOR, "input[name='selected[]']")

    def open(self):
        self.driver.get("http://localhost/admin/index.php?route=catalog/product")

    def delete_first_product(self):
        checkboxes = self.driver.find_elements(*self.PRODUCT_CHECKBOXES)
        if checkboxes:
            checkboxes[0].click()
            self.driver.find_element(*self.DELETE_BUTTON).click()
            alert = self.driver.switch_to.alert
            alert.accept()
