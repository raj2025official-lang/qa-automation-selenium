import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("username,password", [
    ("wrong_user", "wrong_pass"),
    ("standard_user", "wrong_pass"),
    ("", "secret_sauce"),
    ("standard_user", "")
])
def test_invalid_login(driver, username, password):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
    assert error.is_displayed()