import allure
from pages.base_page import BasePage
from locators.tape_order_page_locators import TapeOrderPageLocators


class TapeOrderPage(BasePage):

    @allure.step('Возвращается текст заголовка Ленты заказов')
    def get_text_from_header(self):
        self.wait_visibly_element(TapeOrderPageLocators.TAPE_ORDER_PAGE_HEADER)
        return self.get_text_from_element(TapeOrderPageLocators.TAPE_ORDER_PAGE_HEADER)

    @allure.step('Выполняется клик по ссылке "Конструктор"')
    def click_on_constructor(self):
        self.wait_invisibly_element(TapeOrderPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(TapeOrderPageLocators.CONSTR_LINK)
        self.click_on_element(TapeOrderPageLocators.CONSTR_LINK)

    @allure.step('Возвращается текст заголовка заказа Ленты заказов')
    def get_text_from_order_header_in_tape(self):
        self.wait_visibly_element(TapeOrderPageLocators.ORDER_HEADER_IN_TAPE)
        return self.get_text_from_element(TapeOrderPageLocators.ORDER_HEADER_IN_TAPE)

    @allure.step('Выполняется клик по заказу в ленте')
    def click_on_order_in_tape(self):
        self.wait_invisibly_element(TapeOrderPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(TapeOrderPageLocators.ORDER_IN_TAPE)
        self.click_on_element(TapeOrderPageLocators.ORDER_IN_TAPE)

    @allure.step('Возвращается текст заголовка заказа в окне деталей заказа')
    def get_text_from_order_header_in_detail_window(self):
        self.wait_visibly_element(TapeOrderPageLocators.ORDER_HEADER_IN_DETAIL_WINDOW)
        return self.get_text_from_element(TapeOrderPageLocators.ORDER_HEADER_IN_DETAIL_WINDOW)

    @allure.step('Возвращается текст из блока Состав в окне деталей заказа')
    def get_text_from_composition_in_detail_window(self):
        self.wait_visibly_element(TapeOrderPageLocators.COMPOSITION_IN_DETAIL_WINDOW)
        return self.get_text_from_element(TapeOrderPageLocators.COMPOSITION_IN_DETAIL_WINDOW)

    @allure.step('Возвращается список Номеров заказа в Ленте заказов')
    def get_order_numbers_in_tape(self):
        self.wait_visibly_element(TapeOrderPageLocators.ORDER_IN_TAPE)
        order_number_list = []
        for el in self.find_elements_and_add_to_list(TapeOrderPageLocators.ORDER_NUMBER):
            order_number_list.append(el.text)
        return order_number_list

    @allure.step('Возвращается список Количества заказов за все время и за сегодня в Ленте заказов')
    def get_count_order_in_tape(self):
        self.wait_visibly_element(TapeOrderPageLocators.ORDER_IN_TAPE)
        count_order_list = []
        for el in self.find_elements_and_add_to_list(TapeOrderPageLocators.ORDERS_COUNT):
            count_order_list.append(el.text)
        return count_order_list

    @allure.step('Возвращается список Заказов в блоке "В работе" в Ленте заказов')
    def get_text_from_in_work_order_block(self):
        self.wait_visibly_element(TapeOrderPageLocators.ORDER_IN_WORK_BLOCK)
        self.wait_text_to_be_present_in_element(TapeOrderPageLocators.ORDER_IN_WORK_BLOCK, 'Все текущие заказы готовы!')
        order_in_work_list = []
        for el in self.find_elements_and_add_to_list(TapeOrderPageLocators.ORDER_IN_WORK_BLOCK):
            order_in_work_list.append(int(el.text))
        return order_in_work_list
