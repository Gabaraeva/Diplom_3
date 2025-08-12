import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Детали ингредиента")
class TestIngredientDetails:
    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_modal_displayed()

    @allure.title("Закрытие модального окна")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal()
        assert not main_page.is_modal_displayed()