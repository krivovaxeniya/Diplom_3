from selenium.webdriver.common.by import By

class RecoverPasswordPageLocators:

    EMAIL_FIELD = By.XPATH, ".//input[contains(@class,'text input__textfield')]"
    RECOVER_BUTTON = [By.XPATH, ".//button[text()='Восстановить']"]
    PASSWORD_FIELD = By.XPATH, ".//input[@name='Введите новый пароль']"
    PASSWORD_LABEL_FIELD = By.XPATH, ".//label[contains(@class,'input__placeholder')]"
    LOADING_WINDOW = By.XPATH, ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"
    VISIBLY_PASSWORD_BUTTON = By.XPATH, ".//div[contains(@class,'input__icon')]"
    PASSWORD_TEXT = By.XPATH, ".//input[@class='text input__textfield text_type_main-default']"
    RECOVER_PAGE_HEADER = By.XPATH, ".//div[@class='Auth_login__3hAey']/h2"
