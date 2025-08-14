import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestConstructor:
    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_order_feed()
        main_page.go_to_constructor()
        assert main_page.is_constructor_displayed()

    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_order_feed()
        assert main_page.url_contains("feed")