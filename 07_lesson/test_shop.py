import pytest
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_online_shop():
    driver = webdriver.Chrome()
    shop_page = ShopPage(driver)
    shop_page.authorisation("standard_user", "secret_sauce")
    shop_page.info_and_buttons()
    shop_page.add_items_to_cart(
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
    )
    shop_page.place_order("Mariya", "Timofeeva", "245760")
    total = shop_page.get_result_price()
    assert total == "Total: $58.29"
    shop_page._driver.quit()
