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

def test_constructor_sections(driver):
    # Переход на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Ожидание появления и клик по разделу "Соусы"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))
    ).click()

    # Проверка, что раздел "Соусы" активен (проверяем наличие 'current' в классе)
    sauces_tab = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]"))
    )
    assert 'current' in sauces_tab.get_attribute('class')

    # Ожидание появления и клик по разделу "Начинки"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))
    ).click()

    # Проверка, что раздел "Начинки" активен (проверяем наличие 'current' в классе)
    fillings_tab = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]"))
    )
    assert 'current' in fillings_tab.get_attribute('class')

    # Ожидание появления и клик по разделу "Булки"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Булки']"))
    ).click()

    # Проверка, что раздел "Булки" активен (проверяем наличие 'current' в классе)
    buns_tab = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]"))
    )
    assert 'current' in buns_tab.get_attribute('class')


