from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestStellarburgersConstructor:
    def test_tab_section_bun(self, login):
        driver = login
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.SECTION_COLLECT)))
        element = driver.find_element(*Locators.BUTTON_BUN)
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.BUTTON_BUN)))
        assert 'current' in element.get_attribute('class')


    def test_tab_section_sauce(self, login):
        driver = login
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.SECTION_COLLECT)))
        element = driver.find_element(*Locators.BUTTON_SAUCE)
        element.click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.BUTTON_SAUCE)))
        assert 'current' in element.get_attribute('class')

    def test_tab_section_fill(self, login):
        driver = login
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.SECTION_COLLECT)))
        element = driver.find_element(*Locators.BUTTON_FILL)
        element.click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((Locators.BUTTON_FILL)))
        assert 'current' in element.get_attribute('class')
