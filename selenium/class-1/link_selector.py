import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://parabank.parasoft.com/parabank/i")

driver.maximize_window()
print(driver.title)

driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "got login").click()
time.sleep(3)

driver.quit()
