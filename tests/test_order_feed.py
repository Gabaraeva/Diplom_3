import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Увеличение счетчика заказов")
    def test_order_counters_increase(self, order_feed_page, create_order):
        with allure.step("Получить начальные значения счетчиков"):
            order_feed_page.open()
            orders_total_before = int(order_feed_page.get_orders_total())
            orders_today_before = int(order_feed_page.get_orders_today())

        with allure.step("Создать новый заказ"):
            create_order()

        with allure.step("Обновить страницу и получить новые значения счетчиков"):
            order_feed_page.refresh_page()
            orders_total_after = int(order_feed_page.get_orders_total())
            orders_today_after = int(order_feed_page.get_orders_today())

        with allure.step("Проверить увеличение счетчиков"):
            assert orders_total_after > orders_total_before, "Общий счетчик заказов не увеличился"
            assert orders_today_after > orders_today_before, "Счетчик заказов за сегодня не увеличился"

    @allure.title("Отображение заказа в работе")
    def test_order_in_progress(self, order_feed_page, create_order):
        with allure.step("Создать новый заказ"):
            create_order()

        with allure.step("Открыть ленту заказов"):
            order_feed_page.open()

        with allure.step("Проверить наличие заказа в работе"):
            assert order_feed_page.is_order_in_progress_displayed(), "Заказ в работе не отображается"

        with allure.step("Проверить валидность номера заказа"):
            order_number = order_feed_page.get_orders_in_progress()
            assert order_feed_page.is_valid_order_number(order_number), "Номер заказа в работе невалиден"