from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class OrderFeedPage(BasePage):
    ORDERS_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//div[ul[contains(@class, 'OrderFeed_orderList')]]//li[1]")

    @allure.step("Открыть ленту заказов")
    def open(self):
        super().open("/feed")  # Используем метод базового класса

    @allure.step("Получить общее количество заказов")
    def get_orders_total(self):
        return self.get_text(self.ORDERS_TOTAL).replace(' ', '')

    @allure.step("Получить количество заказов за сегодня")
    def get_orders_today(self):
        return self.get_text(self.ORDERS_TODAY).replace(' ', '')

    @allure.step("Получить номер заказа в работе")
    def get_orders_in_progress(self):
        return self.get_text(self.ORDERS_IN_PROGRESS)