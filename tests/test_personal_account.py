from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestStellarburgersPersonalAccount:
    def test_go_to_personal_account(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_LK).click()

        # Проверяем появление полей формы с данными авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.INPUT_NAME_AUTH_USER)))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.INPUT_LOGIN_AUTH_USER)))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.INPUT_PASS_AUTH_USER)))

        #Проверяем кликабельные пункты меню в Профиле пользователя
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.HR_PROFILE)))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.HR_HISTORY)))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_OUT)))

        #Проверяем кнопки в Профиле пользователя
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_SAVE)))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CANCEL)))

        #Проверяем текст на странице Профиле пользователя
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.TEXT_PROFILE)))




