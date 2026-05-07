from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_add_multiple_products(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    inventory.add_all_items()
    inventory.go_to_cart()

    items = cart.get_items()

    assert len(items) == 6   # Saucedemo has 6 products