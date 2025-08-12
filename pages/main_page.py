from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    CONSTRUCTOR_TAB = (By.XPATH, "//a[span[text()='Конструктор']]")
    ORDER_FEED_TAB = (By.XPATH, "//a[span[text()='Лента Заказов']]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    INGREDIENT_ITEM = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//a[1]")
    INGREDIENT_COUNTER = (By.XPATH,
                          "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']//a[1]//div[contains(@class, 'counter_counter')]")
    MODAL = (By.XPATH, "//div[@class='Modal_modal__P3_V5']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[@class='Modal_modal__P3_V5']/button")
    CONSTRUCTOR_SECTION = (By.ID, "constructor")

    def open(self):
        self.driver.get(f"{self.base_url}/")
        return self

    def go_to_constructor(self):
        self.click(self.CONSTRUCTOR_TAB)

    def go_to_order_feed(self):
        self.click(self.ORDER_FEED_TAB)

    def click_ingredient(self):
        self.click(self.INGREDIENT_ITEM)

    def get_ingredient_counter(self):
        # Если счетчика нет, возвращаем 0
        if self.is_displayed(self.INGREDIENT_COUNTER):
            return self.get_text(self.INGREDIENT_COUNTER)
        return "0"

    def is_modal_displayed(self):
        return self.is_displayed(self.MODAL)

    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    def is_constructor_displayed(self):
        return self.is_displayed(self.CONSTRUCTOR_SECTION)