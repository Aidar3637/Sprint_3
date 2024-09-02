from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_login_from_main_page():
    driver = webdriver.Chrome()
    try:
        # Переход на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидание появления и клик по кнопке "Войти в аккаунт"
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_ACCOUNT)
        ).click()

        # Ввод email
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        ).send_keys("testuser199@yandex.ru")

        # Ввод пароля
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        ).send_keys("password123")

        # Клик по кнопке "Войти"
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_FORM)
        ).click()

        # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
    finally:
        driver.quit()

def test_login_from_account_page():
    driver = webdriver.Chrome()
    try:
        # Переход на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидание появления и клик по кнопке "Личный кабинет"
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # Ввод email
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        ).send_keys("testuser199@yandex.ru")

        # Ввод пароля
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        ).send_keys("password123")

        # Клик по кнопке "Войти"
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_FORM)
        ).click()

        # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
    finally:
        driver.quit()

def test_login_from_registration_page():
    driver = webdriver.Chrome()
    try:
        # Переход на страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Ожидание появления и клик по кнопке "Войти" на странице регистрации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_TEXT)
        ).click()

        # Ввод email
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        ).send_keys("testuser199@yandex.ru")

        # Ввод пароля
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        ).send_keys("password123")

        # Клик по кнопке "Войти"
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_FORM)
        ).click()

        # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
    finally:
        driver.quit()

def test_login_from_password_recovery_page():
    driver = webdriver.Chrome()
    try:
        # Переход на страницу восстановления пароля
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # Ожидание появления и клик по кнопке "Войти" на странице восстановления пароля
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_TEXT)
        ).click()

        # Ввод email
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT)
        ).send_keys("testuser199@yandex.ru")

        # Ввод пароля
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
        ).send_keys("password123")

        # Клик по кнопке "Войти"
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_FORM)
        ).click()

        # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
    finally:
        driver.quit()

