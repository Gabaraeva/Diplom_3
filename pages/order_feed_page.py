from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderFeedPage(BasePage):
    ORDERS_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//div[ul[contains(@class, 'OrderFeed_orderList')]]//li[1]")

    def open(self):
        self.driver.get(f"{self.base_url}/feed")
        return self

    def get_orders_total(self):
        return self.get_text(self.ORDERS_TOTAL)

    def get_orders_today(self):
        return self.get_text(self.ORDERS_TODAY)

    def get_orders_in_progress(self):
        return self.get_text(self.ORDERS_IN_PROGRESS)