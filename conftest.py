import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.open()
    main_page.go_to_login()
    login_page.login("test@example.com", "password")

    # Проверяем успешность логина
    assert main_page.is_constructor_displayed(), "Login failed"
    yield driver


@pytest.fixture
def create_order(driver, login):
    def _create_order():
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_ingredient_to_constructor()
        main_page.click_order_button()
        main_page.confirm_order()
        main_page.wait_for_order_modal()

    return _create_order