import pytest
from pages.site_main_page import SiteMainPage
from pages.auth_page import AuthPage
from pages.personal_account_page import PersonalAccountPage
import requests
from data import Data
import random
import allure


class TestPersonalAccountPage:
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
        response_get_ingr = requests.get(f'{Data.site_main_page}/api/ingredients')
        ingredients = response_get_ingr.json()['data']
        random_ingr_id_1 = random.choice(list(ingredients))['_id']
        random_ingr_id_2 = random.choice(list(ingredients))['_id']
        random_ingr_list = [random_ingr_id_1, random_ingr_id_2]
        payload = {"ingredients": random_ingr_list}
        response = requests.post(f'{Data.site_main_page}/api/orders', headers={'Authorization': cls.user_info.get("token")},
                                 data=payload)
        cls.user_info["order_number"] = response.json()["order"]["number"]

    @allure.title('Проверка перехода по клику на «Личный кабинет» с главной страницы')
    @allure.description(
        'На главной странице сайта выполняется клик по ссылке "Личный кабинет" для авторизованного пользователя, '
        'проверяется переход и соответствие имени пользователя в ЛК указанному при регистрации')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_go_to_personal_account_from_main_page(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        assert personal_account_page.get_text_from_name_field() == self.user_info.get("name")

    @allure.title('Проверка перехода в «Личном кабинете» в раздел «История заказов»')
    @allure.description('На главной странице сайта выполняется клик по ссылке "Личный кабинет" для авторизованного '
                        'пользователя, проверяется переход в раздел "История заказов" и соответствие номера заказа в '
                        'истории созданному заказу для пользователя')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_go_to_personal_account_story_order(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_story_order()
        assert f'#0{self.user_info.get("order_number")}' == personal_account_page.get_text_from_order_number()

    @allure.title('Проверка выхода из аккаунта в «Личном кабинете»')
    @allure.description('На главной странице сайта выполняется клик по ссылке "Личный кабинет" для авторизованного '
                        'пользователя, проверяется переход на страницу авторизации по клику на кнопку "Выход"')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_exit_from_account(self, request, driver_browser, log_in_account):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_to_exit_from_account()
        auth_page = AuthPage(driver)
        assert auth_page.get_text_from_header() == 'Вход'

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Data.site_main_page}/api/auth/user', headers={'Authorization': cls.user_info.get("token")})
