from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import Locators
from tests.constants import Constants

class TestStellarburgersLogin:
    #Вход через кнопку «Личный кабинет»
    def test_login_from_lk_button(self, driver):
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH)))

        driver.find_element(*Locators.INPUT_LOGIN_AUTH).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASS_AUTH).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_AUTH).click()

        WebDriverWait(driver, 7).until(EC.visibility_of_element_located((Locators.BUTTON_LK)))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH_USER)))
        button_out = driver.find_element(*Locators.INPUT_LOGIN_AUTH_USER).get_attribute('value')
        assert button_out == Constants.EMAIL



    #Вход по кнопке «Войти в аккаунт» на главной,
    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.BUTTON_AUTH_MAIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH)))

        driver.find_element(*Locators.INPUT_LOGIN_AUTH).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASS_AUTH).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_AUTH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_LK)))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH_USER)))
        button_out = driver.find_element(*Locators.INPUT_LOGIN_AUTH_USER).get_attribute('value')
        assert button_out == Constants.EMAIL


    #Вход через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.HR_REGISTRATION)))
        driver.find_element(*Locators.HR_REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.HR_AUTH)))
        driver.find_element(*Locators.HR_AUTH).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH)))

        driver.find_element(*Locators.INPUT_LOGIN_AUTH).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASS_AUTH).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_AUTH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_LK)))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH_USER)))
        button_out = driver.find_element(*Locators.INPUT_LOGIN_AUTH_USER).get_attribute('value')
        assert button_out == Constants.EMAIL

    #Вход через кнопку в форме восстановления пароля
    def test_login_from_restore_form(self, driver):
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.HR_RESTORE)))
        driver.find_element(*Locators.HR_RESTORE).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.HR_AUTH)))
        driver.find_element(*Locators.HR_AUTH).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH)))

        driver.find_element(*Locators.INPUT_LOGIN_AUTH).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASS_AUTH).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_AUTH).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_LK)))
        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH_USER)))
        button_out = driver.find_element(*Locators.INPUT_LOGIN_AUTH_USER).get_attribute('value')
        assert button_out == Constants.EMAIL

