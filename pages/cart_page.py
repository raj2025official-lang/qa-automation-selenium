from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    def get_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(e.text.replace("$", "")) for e in elements]

    def is_item_in_cart(self):
        items = self.get_items()
        return len(items) > 0