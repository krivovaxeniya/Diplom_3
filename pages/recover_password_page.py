import allure
from locators.recover_password_locators import RecoverPasswordPageLocators
from pages.base_page import BasePage


class RecoverPasswordPage(BasePage):

    @allure.step('Происходит заполнения поля email на странице восстановления пароля')
    def send_key_on_email_field(self, email):
        self.wait_visibly_element(RecoverPasswordPageLocators.EMAIL_FIELD)
        self.send_keys_to_element(RecoverPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step('Происходит клик по ссылке "Восстановить" на странице восстановления пароля')
    def recover_button_click(self):
        self.click_on_element(RecoverPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Происходит заполнения поля пароль на странице восстановления пароля')
    def send_key_on_password_field(self, password):
        self.wait_visibly_element(RecoverPasswordPageLocators.PASSWORD_FIELD)
        self.send_keys_to_element(RecoverPasswordPageLocators.PASSWORD_FIELD, password)

    @allure.step('Происходит клик на кнопку видимости пароля странице восстановления пароля')
    def visible_password_click(self):
        self.wait_invisibly_element(RecoverPasswordPageLocators.LOADING_WINDOW)
        self.wait_visibly_element(RecoverPasswordPageLocators.VISIBLY_PASSWORD_BUTTON)
        self.click_on_element(RecoverPasswordPageLocators.VISIBLY_PASSWORD_BUTTON)

    @allure.step('Возвращается значение атрибута для поля пароль')
    def get_atribute_from_password_text(self):
        return self.get_attribute_value_from_element(RecoverPasswordPageLocators.PASSWORD_TEXT, 'type')

    @allure.step('Возвращается текст заголовка на странице восстановления пароля')
    def get_text_from_header(self):
        return self.get_text_from_element(RecoverPasswordPageLocators.RECOVER_PAGE_HEADER)

    @allure.step('Возвращается текст плейсхолдера пароля на странице восстановления пароля')
    def get_text_from_password_placeholder(self):
        self.wait_text_to_be_present_in_element(RecoverPasswordPageLocators.PASSWORD_LABEL_FIELD, 'Email')
        return self.get_text_from_element(RecoverPasswordPageLocators.PASSWORD_LABEL_FIELD)
