import pytest
from selenium import webdriver
from data import Data

@pytest.fixture
def driver():
    chromedriver = webdriver.Chrome()
    chromedriver.get(Data.BURGER_URL)
    yield chromedriver
    chromedriver.quit()