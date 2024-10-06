import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Калькулятор")
@allure.title("Тест калькулятора")
@allure.description("Передаем в калькулятор значения и сравниваем ОР и ФР, полученным в калькуляторе")
@allure.severity("Blocker")
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page.enter_delay_value("45")
    calculator_page.click_button("7")
    calculator_page.click_operator_button("+")
    calculator_page.click_button("8")
    calculator_page.click_equals_button()


    result = calculator_page.get_result_text()

    result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()

    with allure.step("Получение результата"):
        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))


    result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()
    with allure.step(
        "Проверяем, что переданный в методе результат сходится с полученным в калькуляторе"
    ):
        assert result == "15"