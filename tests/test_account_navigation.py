import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_go_to_personal_account(driver):
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

    # Ожидание появления и клик по кнопке "Личный кабинет"
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    # Проверка успешного перехода в личный кабинет
    assert WebDriverWait(driver, 3).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
    )


