import pytest
from selenium import webdriver
from data import Data
from pages.site_main_page import SiteMainPage
from pages.auth_page import AuthPage


@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    driver.get(Data.site_main_page)
    driver.fullscreen_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_firefox():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    driver.get(Data.site_main_page)
    yield driver
    driver.quit()


@pytest.mark.parametrize('driver_browser', ['driver_chrome', 'driver_firefox'])
@pytest.fixture(scope='function')
def log_in_account(request, driver_browser):
    driver = request.getfixturevalue(driver_browser)
    site_main_page = SiteMainPage(driver)
    site_main_page.click_on_log_in_account_button()
    auth_page = AuthPage(driver)
    auth_page.send_keys_to_auth_form('krivova_webtest_5@mail.ru', '123456789')
    auth_page.click_on_enter_button()
    return log_in_account
