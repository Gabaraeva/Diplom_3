import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Детали ингредиента")
class TestIngredientDetails:
    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Кликнуть на ингредиент"):
            ingredient_modal = main_page.click_ingredient()

        with allure.step("Проверить отображение модального окна"):
            assert ingredient_modal.is_displayed(), "Модальное окно с деталями ингредиента не отобразилось"

    @allure.title("Закрытие модального окна")
    def test_close_ingredient_modal(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Кликнуть на ингредиент"):
            ingredient_modal = main_page.click_ingredient()

        with allure.step("Закрыть модальное окно"):
            ingredient_modal.close()

        with allure.step("Проверить скрытие модального окна"):
            assert not ingredient_modal.is_displayed(), "Модальное окно не закрылось"