import pytest

from selenium.webdriver.common.by import By

import time

from Pages.HomePage import Home
from Configurations.TestData import TestData


@pytest.mark.smoke
class TestHome:

    @pytest.mark.parametrize("footer_link", TestData.footer_links)
    def test_find_footer_link(self, fixture_setup, footer_link):
        """Checking the existence of links in Footer to external sites"""
        self.driver = fixture_setup
        self.driver.get(TestData.URL)
        time.sleep(3)
        hp = Home(self.driver)
        hp.scroll_page_down()
        footer_link = (By.LINK_TEXT, footer_link)
        text_link = hp.check_text_links(footer_link)
        assert text_link in TestData.footer_links
