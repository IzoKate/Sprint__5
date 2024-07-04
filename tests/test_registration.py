from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import  Locators
from constants import  Constants


class TestStellarburgersRegistration:
    #Проверка успешной Регистрации
    def test_successful_registration(self, driver):

        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH)))

        driver.find_element(*Locators.HR_REGISTRATION).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.INPUT_NAME)))

        driver.find_element(*Locators.INPUT_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL_RANDOM)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_REG).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Locators.BUTTON_AUTH)))
        url = driver.current_url
        assert url == Constants.URL_AUTH


    # Проверка неуспешной регистрации при невалидном пароле
    def test_registration_with_invalid_password(self, driver):

        driver.find_element(*Locators.BUTTON_LK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH)))

        driver.find_element(*Locators.HR_REGISTRATION).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.INPUT_NAME)))

        driver.find_element(*Locators.INPUT_NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL_RANDOM)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD_INVALID)
        driver.find_element(*Locators.BUTTON_REG).click()

        err_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERR_PASSWORD)).text

        assert err_message == 'Некорректный пароль'
