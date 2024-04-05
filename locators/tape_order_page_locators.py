from selenium.webdriver.common.by import By

class TapeOrderPageLocators:

    TAPE_ORDER_PAGE_HEADER = By.XPATH, ".//h1[contains(@class,'text text_type_main-large')]"
    LOADING_WINDOW = By.XPATH, ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"
    CONSTR_LINK = By.XPATH, ".//p[text()='Конструктор']"
    ORDER_HEADER_IN_TAPE = By.XPATH, ".//a[contains(@class,'OrderHistory_link')]/h2[@class='text text_type_main-medium mb-2']"
    ORDER_HEADER_IN_DETAIL_WINDOW = By.XPATH, ".//div[contains(@class,'Modal_orderBox')]/h2[@class='text text_type_main-medium mb-2']"
    COMPOSITION_IN_DETAIL_WINDOW = By.XPATH, ".//div[contains(@class,'Modal_orderBox')]/p[@class='text text_type_main-medium mb-8']"
    ORDER_IN_TAPE = By.XPATH, ".//li[contains(@class,'OrderHistory_listItem')]"
    ORDER_NUMBER = By.XPATH, ".//p[@class='text text_type_digits-default']"
    ORDERS_COUNT = By.XPATH, ".//p[contains(@class,'OrderFeed_number__2MbrQ')]"
    ORDER_IN_WORK_BLOCK = By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li"