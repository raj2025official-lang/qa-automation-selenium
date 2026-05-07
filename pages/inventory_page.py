from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    def add_all_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for item in items:
            item.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()