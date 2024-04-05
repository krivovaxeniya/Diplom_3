import allure
from locators.site_main_page_locators import SiteMainPageLocators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class SiteMainPage(BasePage):

    @allure.step('Выполняется клик на кнопку "Войти в аккаунт"')
    def click_on_log_in_account_button(self):
        self.wait_invisibly_element(SiteMainPageLocators.LOADING_WINDOW)
        self.click_on_element(SiteMainPageLocators.LOG_IN_ACCOUNT_PAGE)

    @allure.step('Выполняется клик по ссылке "Личный кабинет"')
    def click_on_personal_account_button(self):
        self.wait_invisibly_element(SiteMainPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(SiteMainPageLocators.PERSONAL_ACCOUNT_LINK)
        self.click_on_element(SiteMainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Выполняется клик по ссылке "Лента заказов"')
    def click_on_tape_order_link(self):
        self.wait_invisibly_element(SiteMainPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(SiteMainPageLocators.TAPE_ORDER_LINK)
        self.click_on_element(SiteMainPageLocators.TAPE_ORDER_LINK)

    @allure.step('Возвращается текст заголовка Конструктора')
    def get_text_from_header(self):
        self.wait_visibly_element(SiteMainPageLocators.CONSTR_PAGE_HEADER)
        return self.get_text_from_element(SiteMainPageLocators.CONSTR_PAGE_HEADER)

    @allure.step('Возвращается текст наименования ингредиента')
    def get_text_from_ingredient_link(self):
        self.wait_visibly_element(SiteMainPageLocators.INGREDIENT_IN_CONSTRUCTOR)
        return self.get_text_from_element(SiteMainPageLocators.INGREDIENT_IN_CONSTRUCTOR)

    @allure.step('Выполняется клик по Ингредиенту')
    def click_on_ingredient_link(self):
        self.wait_invisibly_element(SiteMainPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(SiteMainPageLocators.INGREDIENT_IN_CONSTRUCTOR)
        self.click_on_element(SiteMainPageLocators.INGREDIENT_IN_CONSTRUCTOR)

    @allure.step('Возвращается текст заголовка в окне деталей ингредиента')
    def get_text_from_detail_window_header(self):
        self.wait_visibly_element(SiteMainPageLocators.HEADER_ON_INGREDIENT_DETAIL_WINDOW)
        return self.get_text_from_element(SiteMainPageLocators.HEADER_ON_INGREDIENT_DETAIL_WINDOW)

    @allure.step('Возвращается текст наименования ингредиента в окне деталей ингредиента')
    def get_text_from_detail_window_ingredient_name(self):
        self.wait_visibly_element(SiteMainPageLocators.NAME_ON_INGREDIENT_DETAIL_WINDOW)
        return self.get_text_from_element(SiteMainPageLocators.NAME_ON_INGREDIENT_DETAIL_WINDOW)

    @allure.step('Возвращается значение атрибута для окна деталей ингредиента')
    def get_class_from_detail_window_section(self):
        return self.get_attribute_value_from_element(SiteMainPageLocators.DETAIL_WINDOW_SECTION, 'class')

    @allure.step('Выполняется клик по крестику в окне деталей ингредиента')
    def click_on_exit_button(self):
        self.wait_invisibly_element(SiteMainPageLocators.LOADING_WINDOW)
        self.wait_clickable_element(SiteMainPageLocators.CLOSE_DETAIL_WINDOW_BUTTON)
        self.click_on_element(SiteMainPageLocators.CLOSE_DETAIL_WINDOW_BUTTON)

    @allure.step('Возвращается текст счетчика количества ингредиента')
    def get_text_from_count_ingredient(self):
        self.wait_visibly_element(SiteMainPageLocators.COUNT_INGREDIENT)
        return self.get_text_from_element(SiteMainPageLocators.COUNT_INGREDIENT)

    @allure.step('Выполняется перемещение ингредиента')
    def drag_and_drop_element(self, element_from, element_to):
        from_element = self.find_element(element_from)
        to_element = self.find_element(element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    @allure.step('Выполняется добавление ингредиента в корзину')
    def add_ingredient_to_basket(self):
        self.find_element_located(SiteMainPageLocators.FLUORESCENT_BUN)
        self.scroll_to_element(SiteMainPageLocators.FLUORESCENT_BUN)
        self.drag_and_drop_element(SiteMainPageLocators.FLUORESCENT_BUN, SiteMainPageLocators.BURGER_BASKET)

    @allure.step('Выполняется добавление ингредиента в корзину и клик на кнопку "Оформить заказ"')
    def create_order(self):
        self.find_element_located(SiteMainPageLocators.FLUORESCENT_BUN)
        self.drag_and_drop_element(SiteMainPageLocators.FLUORESCENT_BUN, SiteMainPageLocators.BURGER_BASKET)
        self.drag_and_drop_element(SiteMainPageLocators.SOUS_SPICY_X, SiteMainPageLocators.BURGER_BASKET)
        self.find_element_located(SiteMainPageLocators.CREATE_ORDER_BUTTON).click()

    @allure.step('Возвращается текст окна создания заказа')
    def get_text_from_order_window(self):
        self.wait_visibly_element(SiteMainPageLocators.ORDER_WINDOW_TEXT)
        return self.get_text_from_element(SiteMainPageLocators.ORDER_WINDOW_TEXT)

    @allure.step('Возвращается номер заказа из окна создания заказа')
    def get_number_from_order_window(self):
        self.wait_text_to_be_present_in_element(SiteMainPageLocators.ORDER_NUMBER_ON_DETAIL_WINDOW, '9999')
        return self.get_text_from_element(SiteMainPageLocators.ORDER_NUMBER_ON_DETAIL_WINDOW)

