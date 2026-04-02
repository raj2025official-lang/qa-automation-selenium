def test_homepage(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title