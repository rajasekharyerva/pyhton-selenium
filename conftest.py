import pytest
import os
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_configure(config):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    allure_results_dir = os.path.join(test_dir, 'allure-results')
    config.option.allure_report_dir = allure_results_dir
