# pages/google_search_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box_locator = (By.NAME, "q")

    def load(self):
        self.driver.get("https://www.google.com")

    def search(self, query):
        search_box = self.driver.find_element(*self.search_box_locator)
        search_box.send_keys(query + Keys.RETURN)

    def get_first_result_text(self):
        first_result = self.driver.find_element(By.CSS_SELECTOR, "h3")
        return first_result.text
