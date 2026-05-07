from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:   # 👈 THIS NAME MUST MATCH EXACTLY

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
    
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        try:
            self.driver.find_element(By.XPATH, "//button[text()='OK']").click() 
        except:
             pass