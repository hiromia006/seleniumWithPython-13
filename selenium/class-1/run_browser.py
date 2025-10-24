import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.saucedemo.com/")

driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.quit()
