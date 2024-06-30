from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import Locators
from tests.constants import Constants

class TestStellarburgersLogout:
    def test_logout(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.BUTTON_OUT)))
        driver.find_element(*Locators.BUTTON_OUT).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.BUTTON_AUTH)))
        assert driver.current_url == Constants.URL_AUTH