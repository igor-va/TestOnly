import pytest

from selenium import webdriver


@pytest.fixture(params=['Chrome'], scope="class")
def fixture_setup(request):
    driver = None
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Firefox":
        driver = webdriver.Firefox()
    return driver
