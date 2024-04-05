import allure
import pytest
from pages.site_main_page import SiteMainPage
from pages.auth_page import AuthPage
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль» на странице '
                  'авторизации')
    @allure.description('Выполняется переход на страницу авторизации по клику на ссылку "Личный кабинет" для '
                        'неавторизованного пользователя, проверяется переход на страницу восстановления пароля по '
                        'нажатию "Восстановить пароль"')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_go_to_recover_password_page(self, request, driver_browser):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_log_in_account_button()
        auth_page = AuthPage(driver)
        auth_page.click_on_recover_password_button()
        recover_password = RecoverPasswordPage(driver)
        assert recover_password.get_text_from_header() == 'Восстановление пароля'

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить" на странице восстановления пароля')
    @allure.description('На странице восстановления пароля указывается почта, выполняется клик на кнопку '
                        '"Восстановить", проверяется переход к блоку восстановления пароля')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_send_email_to_email_field_on_recover_page(self, request, driver_browser):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_log_in_account_button()
        auth_page = AuthPage(driver)
        auth_page.click_on_recover_password_button()
        recover_password = RecoverPasswordPage(driver)
        recover_password.send_key_on_email_field('test_mail@ya.ru')
        recover_password.recover_button_click()
        assert recover_password.get_text_from_password_placeholder() == 'Пароль'

    @allure.title('Проверка клика по кнопке показать/скрыть пароль на странице восстановления пароля')
    @allure.description('На странице восстановления пароля указывается почта, выполняется клик на кнопку '
                        '"Восстановить", вводится пароль, выполняется клик на кнопку видимости пароля. Выполняется '
                        'проверка того, что поле пароля стало текстовым')
    @pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
    def test_check_visibly_password_on_recover_password_page(self, request, driver_browser):
        driver = request.getfixturevalue(driver_browser)
        site_main_page = SiteMainPage(driver)
        site_main_page.click_on_log_in_account_button()
        auth_page = AuthPage(driver)
        auth_page.click_on_recover_password_button()
        recover_password = RecoverPasswordPage(driver)
        recover_password.send_key_on_email_field('test_mail@ya.ru')
        recover_password.recover_button_click()
        recover_password.send_key_on_password_field('123456789')
        recover_password.visible_password_click()
        assert recover_password.get_atribute_from_password_text() == 'text'
