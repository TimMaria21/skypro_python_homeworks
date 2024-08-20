from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

for i in range(3):
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.refresh()


sleep(5)
driver.quit()
