from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    NAME_USER_FIELD = By.XPATH, ".//input[@name='Name']"
    STORY_ORDER_LINK = By.XPATH, ".//a[text()='История заказов']"
    ORDER_NUMBER = By.XPATH, ".//p[@class='text text_type_digits-default']"
    LOADING_WINDOW = By.XPATH, ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ORDER_LIST = By.XPATH, ".//p[@class='text text_type_digits-default']"
    TAPE_ORDER_LINK = By.XPATH, ".//p[text()='Лента Заказов']"
    ORDER_LIST_BLOCK = By.XPATH, './/ul[contains(@class, "OrderHistory_profileList")]'
