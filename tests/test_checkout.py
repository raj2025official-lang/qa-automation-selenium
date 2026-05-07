from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.load()
    login.login("standard_user", "secret_sauce")

    inventory.add_item_to_cart()
    inventory.go_to_cart()

    checkout.click_checkout()
    checkout.enter_details("John", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.is_order_successful()