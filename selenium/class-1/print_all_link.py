import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://parabank.parasoft.com/parabank/")

driver.maximize_window()

all_link = driver.find_elements(By.TAG_NAME, "a")

for link in all_link:
    print(link.text, " ", link.get_attribute("href"))

driver.quit()