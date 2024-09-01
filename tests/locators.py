from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div//input')
    PASSWORD_INPUT = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div//input')
    LOGIN_BUTTON_FORM = (By.XPATH, '/html/body/div/div/main/div/form/button')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '/html/body/div/div/header/nav/a/p')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
    CONSTRUCTOR_HEADER_TEXT = (By.XPATH, '//*[text()="Соберите бургер"]')
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    BUNS_TAB_ACTIVE = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]")
    LOGIN_LINK_TEXT = (By.LINK_TEXT, "Войти")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

