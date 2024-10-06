import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from form_page import FormPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Форма отправки данных")
@allure.title("Тест на заполнение формы")
@allure.description(
    "Заполняем форму тестовыми данными, отправляем, затем считываем результат \
    и сверяем соответствие классов заполненных и незаполненных полей с шаблонами")
@allure.severity("blocker")
def test_form(driver: WebDriver):
    with allure.step("Переход на страницу для заполнения формы"):
        form_page = FormPage(driver)
    with allure.step("Заполнение полей данными"):
        form_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        zip_code="",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )
   
    
    with allure.step(
        "Считываем информацию с полей формы, после её отправки. Собираем информацию о классах."):
        form_page.response_form()

        success_results, danger_results = form_page.get_result()

    with allure.step(
        "Проверяем, что все классы элементов заполненных полей имеют значение - {success_class}, незаполненных полей - {danger_class}"
    ):
        success_class = "alert-success"
        danger_class = "alert-danger"
        with allure.step(
            "В цикле сверяем классы из списка всех заполненных полей с шаблоном"
        ):
            for i in success_results:
                assert success_class in i
        with allure.step(
            "В цикле сверяем классы из списка всех незаполненных полей с шаблоном"
        ):
            for k in danger_results:
                assert danger_class in k
                form_page.driver.quit()