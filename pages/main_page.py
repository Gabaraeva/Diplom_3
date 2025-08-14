from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class MainPage(BasePage):
    CONSTRUCTOR_TAB = (By.XPATH, "//a[span[text()='Конструктор']]")
    ORDER_FEED_TAB = (By.XPATH, "//a[span[text()='Лента Заказов']]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    INGREDIENT_ITEM = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//a[1]")
    INGREDIENT_COUNTER = (By.XPATH,
                          "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//a[1]//div[contains(@class, 'counter_counter')]")
    MODAL = (By.XPATH, "//div[@class='Modal_modal__P3_V5']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[@class='Modal_modal__P3_V5']/button")
    CONSTRUCTOR_SECTION = (By.ID, "constructor")
    INGREDIENT_CONSTRUCTOR = (By.ID, "constructor-area")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Подтвердить заказ')]")
    ORDER_MODAL = (By.CLASS_NAME, "order-modal")

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://stellarburgers.nomoreparties.site"

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(f"{self.base_url}/")

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click(self.CONSTRUCTOR_TAB)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click(self.ORDER_FEED_TAB)

    @allure.step("Перейти на страницу логина")
    def go_to_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(self.INGREDIENT_ITEM)

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        if self.is_displayed(self.INGREDIENT_COUNTER):
            return self.get_text(self.INGREDIENT_COUNTER)
        return "0"

    @allure.step("Проверить видимость модального окна")
    def is_modal_displayed(self):
        return self.is_displayed(self.MODAL)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить видимость конструктора")
    def is_constructor_displayed(self):
        return self.is_displayed(self.CONSTRUCTOR_SECTION)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(self.INGREDIENT_ITEM, self.INGREDIENT_CONSTRUCTOR)

    @allure.step("Нажать кнопку оформления заказа")
    def click_order_button(self):
        self.click(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Ожидать модальное окно заказа")
    def wait_for_order_modal(self):
        self.find_element(self.ORDER_MODAL)