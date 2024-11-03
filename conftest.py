import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    # Basic options first
    options.add_argument("--headless")                   # Run in headless mode
    # Performance-related options
    options.add_argument("--disable-gpu")                # Disable GPU acceleration
    options.add_argument("--disable-dev-shm-usage")     # Overcome limited resource problems
    # Sandbox options last
    options.add_argument("--no-sandbox")                 # Disable the sandbox for testing


# Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def pytest_configure(config):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    allure_results_dir = os.path.join(test_dir, 'allure-results')
    config.option.allure_report_dir = allure_results_dir
