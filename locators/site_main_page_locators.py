from selenium.webdriver.common.by import By


class SiteMainPageLocators:

    LOG_IN_ACCOUNT_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']"
    LOADING_WINDOW = By.XPATH, ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"
    PERSONAL_ACCOUNT_LINK = By.LINK_TEXT, "Личный Кабинет"
    TAPE_ORDER_LINK = By.XPATH, ".//p[text()='Лента Заказов']"
    CONSTR_PAGE_HEADER = By.XPATH, ".//h1[contains(@class,'text text_type_main-large')]"
    INGREDIENT_IN_CONSTRUCTOR = By.XPATH, ".//p[@class ='BurgerIngredient_ingredient__text__yp3dH']"
    HEADER_ON_INGREDIENT_DETAIL_WINDOW = By.XPATH, ".//h2[contains(@class,'Modal_modal__title_modified')]"
    DETAIL_WINDOW_SECTION = By.XPATH, ".//div[@class='App_App__aOmNj']/section"
    NAME_ON_INGREDIENT_DETAIL_WINDOW = By.XPATH, ".//p[contains(@class,'text text_type_main-medium')]"
    CLOSE_DETAIL_WINDOW_BUTTON = By.XPATH, ".//button[contains(@class,'Modal_modal__close')]"
    FLUORESCENT_BUN = By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']"
    SOUS_SPICY_X = By.XPATH, '//*[contains(@class, "BurgerIngredient_ingredient__image") and @alt="Соус Spicy-X"]'
    BURGER_BASKET = By.XPATH, ".//*[contains(@class, 'BurgerConstructor_basket')]"
    COUNT_INGREDIENT = By.XPATH, ".//p[contains(@class,'counter_counter__num__3nue1')]"
    CREATE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    ORDER_WINDOW_TEXT = By.XPATH, ".//div[contains(@class,'Modal_modal__textContainer')]/p[contains(@class,'undefined text text_type_main-small')]"
    ORDER_NUMBER_ON_DETAIL_WINDOW = By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]"
    ORDER_NUMBER_DEFAULT = By.XPATH, ".//h2[@text()='9999']"