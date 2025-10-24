import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.saucedemo.com/")

driver.maximize_window()
print(driver.title)

driver.get("https://parabank.parasoft.com/parabank/")
print(driver.title)
time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(3)

driver.quit()

