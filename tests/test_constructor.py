import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestConstructor:
    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Вернуться в конструктор"):
            main_page.go_to_constructor()

        with allure.step("Проверить отображение конструктора"):
            assert main_page.is_constructor_displayed(), "Конструктор не отображается после перехода"

    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Перейти в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Проверить URL ленты заказов"):
            assert main_page.is_feed_page(), "Не удалось перейти на страницу ленты заказов"