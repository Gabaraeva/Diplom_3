from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента {locator}")
    def is_displayed(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            return True
        except Exception:
            return False

    @allure.step("Ожидать исчезновение элемента {locator}")
    def wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))

    @allure.step("Перетащить элемент {source_locator} на {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить наличие текста {text} в URL")
    def url_contains(self, text):
        return text in self.get_current_url()