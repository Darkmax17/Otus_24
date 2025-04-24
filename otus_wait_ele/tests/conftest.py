import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import allure

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome, firefox, edge")
    parser.addoption("--url", action="store", default="http://localhost/", help="Base URL")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise pytest.UsageError("--browser must be chrome, firefox or edge")

    driver.maximize_window()
    driver.base_url = base_url

    yield driver

    #  Сделать скриншот при падении теста
    if request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Не удалось сохранить скриншот: {e}")

    driver.quit()

# 📌 Подключаем хук pytest_runtest_makereport для анализа результата
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат теста
    outcome = yield
    rep = outcome.get_result()

    # Добавляем результат в объект запроса (request)
    setattr(item, "rep_" + rep.when, rep)
