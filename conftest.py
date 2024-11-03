import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_configure(config):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    allure_results_dir = os.path.join(test_dir, 'allure-results')
    config.option.allure_report_dir = allure_results_dir
