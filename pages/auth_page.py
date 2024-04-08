import allure
from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step('Выполняется клик на кнопку "Восстановить пароль"')
    def click_on_recover_password_button(self):
        self.wait_clickable_element(AuthPageLocators.RECOVER_PASSWORD_BUTTON)
        self.click_on_element(AuthPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Происходит заполнение полей email и пароль на странице авторизации')
    def send_keys_to_auth_form(self, email, password):
        self.wait_visibly_element(AuthPageLocators.AUTH_FORM)
        self.send_keys_to_element(AuthPageLocators.INPUT_EMAIL_FIELD, email)
        self.send_keys_to_element(AuthPageLocators.INPUT_PASSWORD_FIELD, password)

    @allure.step('Выполняется клик на кнопку "Войти"')
    def click_on_enter_button(self):
        self.wait_clickable_element(AuthPageLocators.ENTER_BUTTON)
        self.click_on_element(AuthPageLocators.ENTER_BUTTON)

    @allure.step('Возвращается текст заголовка на странице авторизации')
    def get_text_from_header(self):
        self.wait_visibly_element(AuthPageLocators.AUTH_FORM)
        return self.get_text_from_element(AuthPageLocators.AUTH_PAGE_HEADER)

