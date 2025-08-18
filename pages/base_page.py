from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу по пути '{path}'")
    def open(self, path=""):
        self.driver.get(f"{self.base_url}{path}")

    @allure.step("Найти видимый элемент")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в поле")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить, что URL содержит '{path}'")
    def url_contains(self, path):
        return path in self.get_current_url()

    @allure.step("Принять алерт")
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    @allure.step("Переключиться на iframe")
    def switch_to_frame(self, locator):
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)

    @allure.step("Вернуться к основному контенту")
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    @allure.step("Дождаться загрузки элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )