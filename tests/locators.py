from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    LOGIN_BUTTON_FORM = (By.XPATH, '//button[text()="Войти"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    CONSTRUCTOR_HEADER_TEXT = (By.XPATH, '//*[text()="Соберите бургер"]')
    LOGO_BUTTON = (By.XPATH, '//*[contains(@class, "AppHeader_header__logo")]')
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    BUNS_TAB_ACTIVE = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]")
    LOGIN_LINK_TEXT = (By.LINK_TEXT, "Войти")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.CLASS_NAME, 'input__error')
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Локатор для кнопки "Выход"


