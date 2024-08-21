from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)
input_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
input_field.send_keys("tomsmith")
sleep(2)
input_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
input_field.send_keys("SuperSecretPassword!")
sleep(2)
login = ".radius"
click_login = driver.find_element(By.CSS_SELECTOR, login).click()


sleep(5)
driver.quit()
