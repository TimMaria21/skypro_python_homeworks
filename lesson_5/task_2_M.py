from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(3)
    blue_button = ".btn.btn-primary"
    click_button = driver.find_element(By.CSS_SELECTOR, blue_button).click()
    sleep(3)

sleep(5)
driver.quit()
