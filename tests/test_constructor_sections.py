import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_constructor_sections(driver):
    # Переход на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Ожидание появления и клик по разделу "Соусы"
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.SAUCES_TAB)
    ).click()

    # Проверка, что раздел "Соусы" активен (проверяем наличие 'current' в классе)
    sauces_tab = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.SAUCES_TAB_ACTIVE)
    )
    assert 'current' in sauces_tab.get_attribute('class')

    # Ожидание появления и клик по разделу "Начинки"
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.FILLINGS_TAB)
    ).click()

    # Проверка, что раздел "Начинки" активен (проверяем наличие 'current' в классе)
    fillings_tab = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.FILLINGS_TAB_ACTIVE)
    )
    assert 'current' in fillings_tab.get_attribute('class')

    # Ожидание появления и клик по разделу "Булки"
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Locators.BUNS_TAB)
    ).click()

    # Проверка, что раздел "Булки" активен (проверяем наличие 'current' в классе)
    buns_tab = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.BUNS_TAB_ACTIVE)
    )
    assert 'current' in buns_tab.get_attribute('class')



