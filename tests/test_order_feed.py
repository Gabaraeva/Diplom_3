import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Увеличение счетчика заказов")
    def test_order_counters_increase(self, driver, create_order):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        # Переходим в ленту заказов и запоминаем счетчики
        order_feed_page.open()
        orders_total_before = int(order_feed_page.get_orders_total().replace(' ', ''))
        orders_today_before = int(order_feed_page.get_orders_today().replace(' ', ''))

        # Создаем заказ
        create_order()

        # Обновляем страницу и проверяем счетчики
        driver.refresh()
        orders_total_after = int(order_feed_page.get_orders_total().replace(' ', ''))
        orders_today_after = int(order_feed_page.get_orders_today().replace(' ', ''))

        assert orders_total_after > orders_total_before
        assert orders_today_after > orders_today_before

    @allure.title("Отображение заказа в работе")
    def test_order_in_progress(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        create_order()
        order_feed_page.open()
        order_in_progress = order_feed_page.get_orders_in_progress()
        assert order_in_progress != "" and order_in_progress.isdigit()