from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from constants import Constants

class TestStellarburgersGoToConstructor:
    def test_go_constructor_use_button_constructor(self, login):
        driver = login

        #Проверяем переход по кнопке Конструктор
        driver.find_element(*Locators.BUTTON_LK).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

        #Ждем прогрузку секций конструктора
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.SECTION_COLLECT)))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.SECTION_BURGER_CONSTRUCTOR)))

        assert driver.current_url == Constants.URL

    def test_go_constructor_use_logo_burger(self, login):
        driver = login

        #Проверяем переход по кнопке Конструктор
        driver.find_element(*Locators.BUTTON_LK).click()
        driver.find_element(*Locators.LOGO).click()

        #Ждем прогрузку секций конструктора
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.SECTION_COLLECT)))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.SECTION_BURGER_CONSTRUCTOR)))

        assert driver.current_url == Constants.URL
