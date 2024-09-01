import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_go_to_personal_account(driver):
    # Переход на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Ожидание появления и клик по кнопке "Войти в аккаунт"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    ).click()

    # Ввод email
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div//input'))
    ).send_keys("testuser199@yandex.ru")

    # Ввод пароля
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div//input'))
    ).send_keys("password123")

    # Клик по кнопке "Войти"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/form/button'))
    ).click()

    # Ожидание появления и клик по кнопке "Личный кабинет"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p'))
    ).click()

    # Проверка успешного перехода в личный кабинет
    assert WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile")
    )

    # Ожидание появления и клик по кнопке "Выход" в личном кабинете
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
    ).click()

    # Проверка успешного выхода: ожидание URL страницы входа
    assert WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

