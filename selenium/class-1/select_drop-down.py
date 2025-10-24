import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("asdasdlkasjd")
driver.find_element(By.ID, "mobile").send_keys("012345678912")
driver.find_element(By.ID, "subjects").send_keys("sdfds sdfsd sdf")
driver.find_element(By.ID, "hobbies").click()

sel=Select(driver.find_element(By.ID,"state"))
sel.select_by_index(1)
time.sleep(2)
sel.select_by_value("Rajasthan")
time.sleep(2)
sel.select_by_visible_text("Uttar Pradesh")

time.sleep(2)
driver.quit()