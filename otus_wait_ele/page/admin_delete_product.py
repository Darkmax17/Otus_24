from otus_wait_ele.page.admin_product_page import AdminProductPage

def delete_product(browser):
    page = AdminProductPage(browser)
    page.open()
    page.delete_product_by_name("MacBook Air")  # Название товара
    page.search_product("MacBook Air")
    assert not page.is_product_present("MacBook Air"), "Product was not deleted"
