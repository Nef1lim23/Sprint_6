import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

