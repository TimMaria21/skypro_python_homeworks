import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class FormPage:
    def __init__(self, driver: str) -> None:
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()
    
    @allure.step(
        "Внести данные в форму отправки и отправить её. {first_name}, {last_name}, {address}, {zip_code}, {city}, {country}, {email}, {phone}, {job_position}, {company}"
    )
    def fill_form(
        self,
        first_name: str,
        last_name: str,
        address: str,
        zip_code: str,
        city: str,
        country: str,
        email: str,
        phone: str,
        job_position: str,
        company: str,
    ) -> None:
        """
        Данный метод получает на вход контактные данные, вносит их в
        соответствующие поля и отправляет заполненную форму

        Args:
            first_name (str): имя
            last_name (str): фамилия
            address (str): адрес
            zip_code (str): почтовый индекс
            city (str): город
            country (str): страна
            e_mail (str): адрес электронной почты
            phone_number (str): номер телефона
            job_position (str): должность
            company (str): название организации
        """
        self.driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(company)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        sleep(5)
    
    def response_form(self) -> None:
        """
        Данный метод считывает информацию с полей формы, после её отправки
        """
        self.first_name_new = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        self.last_name_new = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        self.address_new = self.driver.find_element(By.CSS_SELECTOR, "#address")
        self.email_new = self.driver.find_element(By.CSS_SELECTOR, "#e-mail")
        self.phone_new = self.driver.find_element(By.CSS_SELECTOR, "#phone")
        self.zip_code_new = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        self.city_new = self.driver.find_element(By.CSS_SELECTOR, "#city")
        self.country_new = self.driver.find_element(By.CSS_SELECTOR, "#country")
        self.job_position_new = self.driver.find_element( By.CSS_SELECTOR, "#job-position")
        self.company_new = self.driver.find_element(By.CSS_SELECTOR, "#company")
    

    @allure.step("Сохраняем в списки классы заполненных и незаполненных полей")
    def get_result(self) -> list:
        """Данный метод сохраняет в списки классы заполненных и незаполненных полей.

        Returns:
            list: 2 списка с классами полей
        """
        success_results = []
        danger_results = []

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
        )
        fields = [
            self.first_name_new,
            self.last_name_new,
            self.address_new,
            self.email_new,
            self.phone_new,
            self.city_new,
            self.country_new,
            self.job_position_new,
            self.company_new,
        ]

        for element in fields:
            result = element.get_attribute("class")
            success_results.append(result)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-danger"))
        )
        danger_element = self.zip_code_new.get_attribute("class")
        danger_results.append(danger_element)

        return success_results, danger_results