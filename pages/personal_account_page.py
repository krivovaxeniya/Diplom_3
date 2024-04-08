import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Возвращается текст поля "Имя пользователя" в личном кабинете')
    def get_text_from_name_field(self):
        self.wait_visibly_element(PersonalAccountPageLocators.NAME_USER_FIELD)
        return self.get_attribute_value_from_element(PersonalAccountPageLocators.NAME_USER_FIELD, 'value')

    @allure.step('Происходит переход по ссылке "История заказов" в личном кабинете')
    def go_to_story_order(self):
        self.wait_invisibly_element(PersonalAccountPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(PersonalAccountPageLocators.STORY_ORDER_LINK)
        self.click_on_element(PersonalAccountPageLocators.STORY_ORDER_LINK)
        self.wait_visibly_element(PersonalAccountPageLocators.ORDER_LIST_BLOCK)

    @allure.step('Возвращается Номер заказа в истории заказов')
    def get_text_from_order_number(self):
        self.wait_visibly_element(PersonalAccountPageLocators.ORDER_NUMBER)
        return self.get_text_from_element(PersonalAccountPageLocators.ORDER_NUMBER)

    @allure.step('Происходит клик по ссылке "Выход" в личном кабинете')
    def click_to_exit_from_account(self):
        self.wait_invisibly_element(PersonalAccountPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(PersonalAccountPageLocators.EXIT_BUTTON)
        self.click_on_element(PersonalAccountPageLocators.EXIT_BUTTON)

    @allure.step('Возвращается список Номеров заказа в истории заказов')
    def get_order_numbers_in_personal_account(self):
        order_number_list = []
        for el in self.find_elements_and_add_to_list(PersonalAccountPageLocators.ORDER_LIST):
            order_number_list.append(el.text)
        return order_number_list

    @allure.step('Происходит клик по ссылке "Лента заказов" в шапке страницы из личного кабинета')
    def click_on_tape_order_link(self):
        self.wait_invisibly_element(PersonalAccountPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(PersonalAccountPageLocators.TAPE_ORDER_LINK)
        self.click_on_element(PersonalAccountPageLocators.TAPE_ORDER_LINK)


