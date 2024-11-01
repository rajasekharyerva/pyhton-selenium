import pytest
import allure
import os
from pages.google_search_page import GoogleSearchPage


@allure.feature("Google Search")
@allure.story("Search Functionality")
@allure.title("Test Search Data")
def test_google_search_contains_query(browser):
    query = "Selenium Python"
    google_search_page = GoogleSearchPage(browser)

    google_search_page.load()
    google_search_page.search(query)

    # Verify that the first result contains the search text
    first_result_text = google_search_page.get_first_result_text()
    assert query in first_result_text, f"Expected '{query}' to be in '{first_result_text}'"
