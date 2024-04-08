from selenium.webdriver.common.by import By


class AuthPageLocators:

    RECOVER_PASSWORD_BUTTON = [By.LINK_TEXT, "Восстановить пароль"]
    AUTH_FORM = By.XPATH, './/div[@class="Auth_login__3hAey"]'
    INPUT_EMAIL_FIELD = By.NAME, "name"
    INPUT_PASSWORD_FIELD = By.NAME, "Пароль"
    ENTER_BUTTON = By.XPATH, ".//button[text()='Войти']"
    AUTH_PAGE_HEADER = By.XPATH, ".//div[@class='Auth_login__3hAey']/h2"
