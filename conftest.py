import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.test_data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def logged_in_driver(driver, main_page, login_page):
    main_page.open()
    main_page.go_to_login()
    login_page.login(TestData.VALID_EMAIL, TestData.VALID_PASSWORD)
    return driver