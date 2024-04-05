import allure
import pytest
from pages.site_main_page import SiteMainPage
from pages.tape_order_page import TapeOrderPage
from pages.personal_account_page import PersonalAccountPage
import requests
from data import Data


class TestTapeOrderPage:
    user_info = {}

    @classmethod
    def setup_class(cls):
        payload = {
            "email": f'krivova_webtest_5@mail.ru',
            "password": '123456789',
            "name": 'Xeniya'}
        response_registration = requests.post(f'{Data.site_main_page}/api/auth/register', data=payload)
        if response_registration.status_code == 200:
            cls.user_info = {"email": payload.get('email'),
                             "password": payload.get('password'),
                             "name": payload.get('name'),
                             "token": response_registration.json()["accessToken"]}

    @allure.title('Проверка перехода по клику на «Лента заказов» в шапке страницы')
    @allure.description('На главной странице сайта выполняется клик по ссылке "Лента заказов", выполняется проверка '
                        'перехода к ленте заказов')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_go_to_tape_order_page_from_main_page(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        assert tape_order_page.get_text_from_header() == 'Лента заказов'

    @allure.title('Проверка открытия всплывающего окна с деталями заказа по клику на заказ в ленте')
    @allure.description('В ленте заказов производится клик на заказ. Выполняется проверка открытия окна с деталями '
                        'выбранного заказ')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_open_window_with_order_details(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        header_order_in_tape = tape_order_page.get_text_from_order_header_in_tape()
        tape_order_page.click_on_order_in_tape()
        header_order_in_detail_window = tape_order_page.get_text_from_order_header_in_detail_window()
        assert header_order_in_tape == header_order_in_detail_window and tape_order_page.get_text_from_composition_in_detail_window() == 'Cостав'

    @allure.title('Проверка наличия заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    @allure.description('Из истории заказов в личном кабинете пользователя собираются номера заказа. Выполняется '
                        'переход на ленту заказов. Проверяется наличие заказов из истории пользователя в ленте')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_check_user_orders_from_personal_account_in_order_tape(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.create_order()
        site_main_page.click_on_exit_button()
        site_main_page.click_on_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_story_order()
        order_number_from_personal_account = personal_account_page.get_order_numbers_in_personal_account()
        personal_account_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        order_number_from_tape = tape_order_page.get_order_numbers_in_tape()
        for number in order_number_from_personal_account:
            assert number in order_number_from_tape

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" в ленте заказов при создании нового заказа')
    @allure.description('В ленте заказов берется значения счетчика "Выполнено за всё время". Выполняется переход в '
                        'конструктор, создается новый заказ. Происходит переход в ленту заказов, выполняется проверка '
                        'того, что счетчик заказов увеличен на 1')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_create_order_change_count_in_all_orders(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        count_order_all_before = int(tape_order_page.get_count_order_in_tape()[0])
        tape_order_page.click_on_constructor()
        site_main_page = SiteMainPage(driver)
        site_main_page.create_order()
        site_main_page.click_on_exit_button()
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        count_order_all_after = int(tape_order_page.get_count_order_in_tape()[0])
        assert count_order_all_before + 1 == count_order_all_after

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" в ленте заказов при создании нового заказа')
    @allure.description('В ленте заказов берется значения счетчика "Выполнено за сегодня". Выполняется переход в '
                        'конструктор, создается новый заказ. Происходит переход в ленту заказов, выполняется проверка '
                        'того, что счетчик заказов увеличен на 1')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_create_order_change_count_in_today_orders(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        count_order_all_before = int(tape_order_page.get_count_order_in_tape()[1])
        tape_order_page.click_on_constructor()
        site_main_page = SiteMainPage(driver)
        site_main_page.create_order()
        site_main_page.click_on_exit_button()
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        count_order_all_after = int(tape_order_page.get_count_order_in_tape()[1])
        assert count_order_all_before + 1 == count_order_all_after

    @allure.title('Проверка наличия номера заказа в разделе "В работе" после создания заказа')
    @allure.description('В конструкторе оформляется новый заказ, сохраняется значение его номера. Выполняется переход '
                        'в ленту заказов. Проверяется добавление номера нового заказа в раздел "В работе"')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_check_new_order_in_block_in_work(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.create_order()
        number_order = int(site_main_page.get_number_from_order_window())
        site_main_page.click_on_exit_button()
        site_main_page.click_on_tape_order_link()
        tape_order_page = TapeOrderPage(driver)
        assert number_order in tape_order_page.get_text_from_in_work_order_block()

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Data.site_main_page}/api/auth/user', headers={'Authorization': cls.user_info.get("token")})