from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element_text(self, element):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(element)).text
