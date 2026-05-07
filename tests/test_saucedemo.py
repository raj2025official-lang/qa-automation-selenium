from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_saucedemo_purchase(driver):

    # Step 1: Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()

    # Step 3: Go to cart
    inventory.go_to_cart()

    # Step 4: Verify
    cart = CartPage(driver)
    assert cart.is_item_in_cart()