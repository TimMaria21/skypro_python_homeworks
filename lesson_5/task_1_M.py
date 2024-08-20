from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
button = "/html/body/div[2]/div/div/button"
click_button = driver.find_element(By.XPATH, button)
for new_element in range(1, 6):
    click_button.click()
    sleep(1)

button_delete = ".added-manually"
button_list = driver.find_elements(By.CSS_SELECTOR, button_delete)

print(len(button_list))

sleep(3)
driver.quit()
