import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(Constants.URL)
    yield browser

    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_LK).click()
    driver.find_element(*Locators.INPUT_LOGIN_AUTH).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.INPUT_PASS_AUTH).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.BUTTON_AUTH).click()
    return driver