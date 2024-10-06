from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ShopPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)


    @allure.step("Авторизация пользователя {name}:{password}")
    def authorisation(self, name: str, password: str) -> None:
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()


    def info_and_buttons(self) -> None:
        self.add_to_cart = self._driver.find_elements(
            By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory"
        )
        self.item_names = self._driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_name"
        )
        self.prices = self._driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_price"
        )

    @allure.step("Сравнивание на соответсвия добавленных в корзину товаров их наиминованию")
    def add_items_to_cart(self, name_item1: str, name_item2: str, name_item3: str) -> None:
        """
        Данный метод сверяет переданные наименования товаров с товарами
        на сайте и добавляет необходимые товары в корзину, согласно
        переданным наименованиям.

        Args:
            name_item1 (str): наименование первого товара
            name_item2 (str): наименование второго товара
            name_item3 (str): наименование третьего товара
        """
        item1_button = None
        item2_button = None
        item3_button = None
            
        for i in range(len(self.item_names)):
            item = self.item_names[i]
            if item.text == name_item1 and not item1_button:
                item1_button = self.add_to_cart[i]
            elif item.text == name_item2 and not item2_button:
                item2_button = self.add_to_cart[i]
            elif item.text == name_item3 and not item3_button:
                item3_button = self.add_to_cart[i]
                    
        if item1_button and item2_button and item3_button:
            item1_button.click()
            item2_button.click()
            item3_button.click()


    @allure.step("Ввод данных покупателя")
    def place_order(self, first_name: str, last_name: str, zip_code: int) -> None:
        """
        Данный метод переводит в корзину и оформляет заказ.

        Args:
            first_name (str): имя
            last_name (str): фамилия
            zip_code (int): почтовый индекс
        """
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()


    @allure.step("Высчитывание итоговой стоимости товаров")
    def get_result_price(self) -> str:
        """
        Данный метод считывает итоговую стоимость
        товаров на странице оформления заказа.

        Returns:
            str: текст из поля стоимости
        """
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        ).text
        return total