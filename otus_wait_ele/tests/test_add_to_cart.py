import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_random_product_to_cart(browser):
    # 1. Открываем главную
    browser.get(browser.base_url)
    wait = WebDriverWait(browser, 30)

    # 2. Собираем все товары на странице
    products = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".product-layout")))
    assert products, "На главной нет ни одного товара"

    # 3. Выбираем случайный товар и запоминаем его название
    product = random.choice(products)
    product_name = product.find_element(By.CSS_SELECTOR, "h4 a").text

    # 4. Нажимаем «Add to Cart»
    add_btn = product.find_element(By.CSS_SELECTOR, "button[onclick*='cart.add']")
    add_btn.click()

    # 5. Ждём уведомления об успешном добавлении
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")))

    # 6. Открываем корзину и переходим в «View Cart»
    cart_btn = browser.find_element(By.ID, "cart")
    cart_btn.click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))).click()

    # 7. Проверяем, что наш товар присутствует в корзине
    cart_table = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".table-responsive")))
    assert product_name in cart_table.text, f"Товар {product_name} не найден в корзине"