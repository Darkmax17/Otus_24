import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_random_product_to_cart(browser):
    # 1. Явно задаём base_url (не через getattr!)
    browser.get(base_url)
    wait = WebDriverWait(browser, 30)

    # 2. Ждём наличие товаров, с прокруткой
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    try:
        # Ожидаем хотя бы один товар
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-thumb")))
        products = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
    except Exception as e:
        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(browser.page_source)
        raise AssertionError("Не найдено ни одного товара. HTML сохранён в debug.html") from e

    assert products, "Товары не найдены"

    # 3. Выбор случайного товара
    product = random.choice(products)
    product_name = product.find_element(By.CSS_SELECTOR, "h4 a").text.strip()
    print(f"Выбран товар: {product_name}")

    # 4. Клик на кнопку "Add to Cart"
    try:
        add_btn = product.find_element(By.XPATH, ".//button[@aria-label='Add to Cart']")
        add_btn.click()
    except Exception as e:
        with open("debug_button.html", "w", encoding="utf-8") as f:
            f.write(product.get_attribute("outerHTML"))
        raise AssertionError("Кнопка Add to Cart не найдена или не кликнулась") from e

    # 5. Ждём появления alert'а с подтверждением
    try:
        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success")))

        # Ждём, пока alert станет полностью видимым (opacity == 1)
        wait.until(lambda driver: float(alert.value_of_css_property("opacity")) >= 0.99)

        # Ищем ссылку перехода в корзину и кликаем
        cart_link = alert.find_element(By.XPATH, ".//a[contains(@href, 'route=checkout/cart')]")
        cart_link.click()

    except Exception as e:
        with open("debug_alert.html", "w", encoding="utf-8") as f:
            f.write(browser.page_source)
        raise AssertionError("Не удалось найти или кликнуть ссылку 'shopping cart'") from e

