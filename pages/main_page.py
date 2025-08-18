from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_SECTION = (By.XPATH, "//h1[text()='Соберите бургер']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account']")
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']")
    INGREDIENT_ITEM = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients')]//a[1]")
    MODAL_CONTAINER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")

    @allure.step("Открыть главную страницу")
    def open(self):
        super().open("/")

    @allure.step("Перейти к странице логина")
    def go_to_login(self):
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Проверить видимость конструктора")
    def is_constructor_displayed(self):
        return self.is_element_visible(self.CONSTRUCTOR_SECTION)

    @allure.step("Перейти в профиль")
    def go_to_profile(self):
        self.click_element(self.PROFILE_LINK)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_element(self.ORDER_FEED_LINK)
        return self.driver.current_url

    @allure.step("Вернуться в конструктор")
    def go_to_constructor(self):
        self.click_element(self.CONSTRUCTOR_LINK)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_element(self.INGREDIENT_ITEM)

    @allure.step("Проверить отображение модального окна")
    def is_modal_displayed(self):
        return self.is_element_visible(self.MODAL_CONTAINER)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        close_button = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
        self.click_element(close_button)