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

    @allure.step("Открываем страницу каталога продуктов")
    def open(self):
        self.driver.get("http://localhost/admin/index.php?route=catalog/product")

    @allure.step("Удаляем первый продукт из списка")
    def delete_first_product(self):
        checkboxes = self.driver.find_elements(*self.PRODUCT_CHECKBOXES)
        if checkboxes:
            checkboxes[0].click()
            self.driver.find_element(*self.DELETE_BUTTON).click()
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except NoAlertPresentException:
                allure.attach(self.driver.get_screenshot_as_png(), name="no_alert_present", attachment_type=allure.attachment_type.PNG)
                raise AssertionError("Ожидался alert при удалении, но он не появился")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="no_product_found", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Нет доступных продуктов для удаления")