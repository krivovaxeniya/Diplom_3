from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_visibly_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    def wait_clickable_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    def wait_invisibly_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element(locator))

    def wait_text_to_be_present_in_element(self, locator, text):
        return WebDriverWait(self.driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    def click_on_element(self, locator):
        self.wait_clickable_element(locator)
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        self.wait_visibly_element(locator)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_keys_to_element(self, locator, value):
        element = self.find_element(locator)
        element.send_keys(value)

    def get_attribute_value_from_element(self, locator, atribute_name):
        return self.find_element(locator).get_attribute(atribute_name)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def find_elements_and_add_to_list(self, locator):
        return self.driver.find_elements(*locator)

    def find_element_located(self, element, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(element))


