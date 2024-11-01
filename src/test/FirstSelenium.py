import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


@allure.feature("Google Search")
@allure.story("Search Functionality")
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Test Search Data")
def test_search_data(browser):
    search_text = "Selenium Python"

    # Open Google
    browser.get("http://www.google.com")

    # Find the search box
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys(search_text + Keys.RETURN)  # Perform search

    # Verify that the first result contains the search text
    first_result = browser.find_element(By.CSS_SELECTOR, 'h3')
    assert search_text in first_result.text, f"Expected '{search_text}' to be in the first result text."


def test_get_title_after_search(browser):
    search_text = "Selenium Python"

    # Open Google
    browser.get("http://www.google.com")

    # Find the search box
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys(search_text + Keys.RETURN)  # Perform search

    # Verify the title of the page after search
    expected_title = f"{search_text} - Google Search"
    assert browser.title == expected_title, f"Expected title to be '{expected_title}', but got '{browser.title}'."


if __name__ == "__main__":
    pytest.main()
