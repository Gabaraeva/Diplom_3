import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param
    if browser == 'chrome':
        options = ChromeOptions()
        # options.add_argument('--headless')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        # options.add_argument('-headless')
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def create_order(driver):
    # Реализация создания заказа
    def _create_order():
        # Здесь будет код для создания заказа
        print("Создание заказа")
        # Добавьте реальную логику создания заказа здесь
    return _create_order