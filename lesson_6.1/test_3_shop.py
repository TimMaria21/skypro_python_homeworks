import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_internet_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    # переход на другую страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.inventory_item_img"))
    )
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    # переход на другую страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button#checkout"))
    )
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    # переход на другую страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input#first-name"))
    )
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Mariya")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Timofeeva")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(245760)
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    # переход на другую страницу
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.summary_total_label"))
    )
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    print(total)
    assert total == "Total: $58.29"
    driver.quit()
   