from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver: str) -> None:
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_page(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Задать время")
    def enter_delay_value(self, delay_value: int) -> int:
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    @allure.step("Нажать на кнопку с цифрой")
    def click_button(self, button_text: None) -> int:
        button_locator = f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    @allure.step("Нажать на кнопку '+'")
    def click_operator_button(self, operator: None) -> str:
        operator_locator = f"//span[contains(@class, 'operator') and text()='{operator}']"
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    @allure.step("Нажать  на кнопку '='")
    def click_equals_button(self) -> int:
        equals_locator = "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()

    @allure.step("Ожидание перед получением результата")
    def get_result_text(self):
        result_element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen"))
        )
        return result_element.text
    