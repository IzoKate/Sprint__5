from selenium.webdriver.common.by import By

class Locators:
    # Кнопка Личный кабинет на главной странице
    BUTTON_LK = (By.XPATH, ".//a[@href='/account']")

    # Кнопка Зарегистрироваться на форме регистрации
    BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    #Кнопка Войти на форме Авторизации
    BUTTON_AUTH = (By.XPATH,".//button[text()='Войти']")

    #Кнопка Войти на Главной странице
    BUTTON_AUTH_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    #Кнопка Выйти в Профиле пользователя
    BUTTON_OUT = (By.XPATH, ".//button[text()='Выход']")

    #Кнопка Сохранить в Профиле пользователя
    BUTTON_SAVE = (By.XPATH, ".//button[text()='Сохранить']")

    #Кнопка Отмена в Профиле пользователя
    BUTTON_CANCEL = (By.XPATH, ".//button[text()='Отмена']")

    #Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    #Кнопка Булки
    BUTTON_BUN = (By.XPATH,".//span[text()='Булки']/parent::div")

    #Кнопка Соусы
    BUTTON_SAUCE = (By.XPATH,".//span[text()='Соусы']/parent::div")

    #Кнопка Начинки
    BUTTON_FILL = (By.XPATH,".//span[text()='Начинки']/parent::div")

    #Кликабельная ссылка Зарегистрироваться на форме входа в аккаунт
    HR_REGISTRATION = (By.XPATH, ".//a[@href='/register']")

    #Кликабельная ссылка Войти на форме Регистрации и форме Восстановления пароля
    HR_AUTH = (By.XPATH,".//a[@href='/login']")

    # Кликабельная ссылка Восстановить пароль на форме входа в аккаунт
    HR_RESTORE = (By.XPATH, ".// a[ @ href = '/forgot-password']")

    # Кликабельная ссылка Профиль в профиле авторизованного пользователя
    HR_PROFILE = (By.XPATH, ".//a[@href='/account/profile']")

    # Кликабельная ссылка История заказов в профиле авторизованного пользователя
    HR_HISTORY = (By.XPATH, ".//a[@href='/account/order-history']")

    # Поле ввода Имя на форме регистрации
    INPUT_NAME = (By.XPATH, ".//fieldset[1]/div/div/input")

    # Поле ввода E-mail на форме регистрации
    INPUT_EMAIL = (By.XPATH, ".//fieldset[2]/div/div/input")

    # Поле ввода Пароль на форме регистрации
    INPUT_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    #Поле ввода логин на форме авторизации
    INPUT_LOGIN_AUTH = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    #Поле ввода пароля на форме авторизации
    INPUT_PASS_AUTH = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    #Поле ввода с логином в Профиле авторизованного пользователя
    INPUT_LOGIN_AUTH_USER = (By.XPATH, ".//label[text()='Логин']/following-sibling::input")

    #Поле ввода с именем в Профиле авторизованного пользователя
    INPUT_NAME_AUTH_USER = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")

    #Поле ввода с паролем в Профиле авторизованного пользователя
    INPUT_PASS_AUTH_USER = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    #Секция Конструктора "Соберите бургер"
    SECTION_COLLECT = (By.XPATH, ".//main[1]/section[1]")

    # Секция Конструктор бургера
    SECTION_BURGER_CONSTRUCTOR = (By.XPATH,".//main[1]/section[2]")

    # Кликабельный логотип Stellar Burgers
    LOGO = (By.XPATH, ".//div/a[@href='/']/*[name()='svg']")

    #Ошибка регистрации, если пароль навалидный
    ERR_PASSWORD = (By.XPATH,".//p[@class='input__error text_type_main-default']")

    #Текстовое поле на странице Профиля пользователя
    TEXT_PROFILE = (By.XPATH, ".//p[starts-with(text(), 'В этом')]")



