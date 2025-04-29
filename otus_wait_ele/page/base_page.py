from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        logger.info(f"Clicking on element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        logger.info(f"Inputting text '{text}' into element: {locator}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        logger.info(f"Getting text from element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_present(self, locator):
        try:
            logger.info(f"Checking presence of element: {locator}")
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def find(self, locator):
        logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def finds(self, locator):
        logger.info(f"Finding all elements matching: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until_visible(self, locator):
        logger.info(f"Waiting for element to be visible: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_disappears(self, locator):
        logger.info(f"Waiting for element to disappear: {locator}")
        self.wait.until(EC.invisibility_of_element_located(locator))