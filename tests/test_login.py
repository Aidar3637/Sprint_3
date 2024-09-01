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


def test_login_from_main_page(driver):
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

    # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )


def test_login_from_account_page(driver):
    # Переход на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Ожидание появления и клик по кнопке "Личный кабинет"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p'))
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
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
    ).click()

    # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )


def test_login_from_registration_page(driver):
    # Переход на страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ожидание появления и клик по кнопке "Войти" на странице регистрации
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))
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
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
    ).click()

    # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )

def test_login_from_password_recovery_page(driver):
    # Переход на страницу восстановления пароля
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # Ожидание появления и клик по кнопке "Войти" на странице восстановления пароля
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))
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
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
    ).click()

    # Проверка успешного входа: проверяем наличие кнопки "Оформить заказ"
    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )

