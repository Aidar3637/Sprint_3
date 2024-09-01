import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver
    driver.quit()

def generate_random_string(length=8):
    """Генерирует случайную строку из букв и цифр."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def test_registration_flow(driver):
    random_name = generate_random_string()
    random_email = f"{random_name}@yandex.ru"

    # 1. Успешная регистрация
    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div//input'))
    ).send_keys(random_name)

    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div//input'))
    ).send_keys(random_email)

    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div//input'))
    ).send_keys("password123")

    WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
    ).click()

    assert WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/button'))
    )

    # Завершаем успешную регистрацию и начинаем новую проверку

    driver.get("https://stellarburgers.nomoreparties.site/register")

    # 2. Регистрация с некорректным паролем
    random_name = generate_random_string()
    random_email = f"{random_name}@yandex.ru"

    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div//input'))
    ).send_keys(random_name)

    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div//input'))
    ).send_keys(random_email)

    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div//input'))
    ).send_keys("short")

    WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
    ).click()

    # Проверка наличия ошибки
    error_message = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'input__error'))
    )
    assert error_message.is_displayed()


