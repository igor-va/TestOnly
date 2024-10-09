from selenium.webdriver import ActionChains

from .BasePage import BasePage


class Home(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_text_links(self, link_page):
        return BasePage.get_element_text(self, element=link_page)

    def scroll_page_down(self):
        ActionChains(self.driver).scroll_by_amount(0, 20000).perform()
