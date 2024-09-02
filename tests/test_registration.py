import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from locators import Locators

def generate_random_string(length=8):
    """Генерирует случайную строку из букв и цифр."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def test_registration_flow(driver):
    random_name = generate_random_string()
    random_email = f"{random_name}@yandex.ru"

    driver.get("https://stellarburgers.nomoreparties.site/register")

    # 1. Успешная регистрация
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.NAME_INPUT)
    ).send_keys(random_name)

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    ).send_keys(random_email)

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
    ).send_keys("password123")

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    ).click()

    assert WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.LOGIN_BUTTON_FORM)
    )

    # Завершаем успешную регистрацию и начинаем новую проверку

    driver.get("https://stellarburgers.nomoreparties.site/register")

    # 2. Регистрация с некорректным паролем
    random_name = generate_random_string()
    random_email = f"{random_name}@yandex.ru"

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.NAME_INPUT)
    ).send_keys(random_name)

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    ).send_keys(random_email)

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.PASSWORD_INPUT)
    ).send_keys("short")

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    ).click()

    # Проверка наличия ошибки
    error_message = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.ERROR_MESSAGE)
    )
    assert error_message.is_displayed()


