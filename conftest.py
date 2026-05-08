import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()

    # 🔥 THIS LINE IS THE REAL FIX
    options.add_argument("--guest")

    # extra safety
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()