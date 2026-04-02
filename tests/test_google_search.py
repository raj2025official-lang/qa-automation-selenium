from selenium.webdriver.common.by import By

def test_python_org_search(driver):
    driver.get("https://www.python.org")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium")
    search_box.submit()

    assert "Python" in driver.title or "Search" in driver.title