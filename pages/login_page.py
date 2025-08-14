from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Ввести email {email}")
    def enter_email(self, email):
        self.find_element(self.EMAIL_INPUT).send_keys(email)

    @allure.step("Ввести пароль {password}")
    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step("Нажать кнопку входа")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()