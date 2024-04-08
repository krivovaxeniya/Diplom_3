import pytest
from pages.site_main_page import SiteMainPage
from pages.tape_order_page import TapeOrderPage
from create_data import *


class TestTapeOrderPage:
    user_info = {}

    @classmethod
    def setup_class(cls):
        cls.user_info = register_new_user_and_return_user_info()

    @allure.title('Проверка перехода по клику на «Конструктор» в шапке страницы')
    @allure.description('На главной странице сайта выполняется клик по ссылке "Лента заказов", затем клик по ссылке '
                        '"Конструктор", выполняется проверка перехода в конструктор заказа')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_go_to_tape_order_page_from_main_page(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        tape_order_page.click_on_constructor()
        assert site_main_page.get_text_from_header() == 'Соберите бургер'

    @allure.title('Проверка всплывающего окна с деталями ингредиента по клику на ингредиент в Конструкторе')
    @allure.description('В конструкторе заказов производится клик на игредиент. Выполняется проверка открытия окна с '
                        'деталями выбранного ингредиента')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_click_on_ingredient_name_open_detail_window(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        name_text_on_constructor = site_main_page.get_text_from_ingredient_link()
        site_main_page.click_on_ingredient_link()
        header_text = site_main_page.get_text_from_detail_window_header()
        name_text_on_detail_window = site_main_page.get_text_from_detail_window_ingredient_name()
        class_section = site_main_page.get_class_from_detail_window_section()
        assert header_text == 'Детали ингредиента' and name_text_on_detail_window == name_text_on_constructor and 'opened' in class_section

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик')
    @allure.description('В конструкторе заказов производится клик на игредиент, в окне с деталями ингредиента '
                        'производится клик на крестик. Выполняется проверка того, что окно с деталями перестает быть '
                        'открытым')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_close_detail_window(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_ingredient_link()
        site_main_page.click_on_exit_button()
        class_section = site_main_page.get_class_from_detail_window_section()
        assert 'opened' not in class_section

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ')
    @allure.description('В конструкторе ингредиент булка перетаскивается в корзину. Проверяется то, что в счетчике '
                        'ингредиента количество стало равным 2')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_add_ingredient_in_basket_check_count(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.add_ingredient_to_basket()
        assert site_main_page.get_text_from_count_ingredient() == '2'

    @allure.title('Проверка создания заказа')
    @allure.description('Авторизованный пользователь добавляет ингредиенты в корзину и нажимает на "Создать заказ". '
                        'Выполняется проверка появления окна создания заказа')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_create_order(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.create_order()
        assert site_main_page.get_text_from_order_window() == 'Ваш заказ начали готовить'

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Data.site_main_page}{Data.endpoint_delete_user}', headers={'Authorization': cls.user_info.get("token")})
