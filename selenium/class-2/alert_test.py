import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "button[onclick='showAlert()']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"button[onclick='myDesk()']").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@onclick='myPromp()']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Selenium Alert Prompt")
time.sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(2)

# Optimize code
driver.find_element(By.XPATH, "//button[@onclick='myPromp()']").click()
at=driver.switch_to.alert
time.sleep(2)
at.send_keys("Selenium Alert Prompt")
time.sleep(2)
print(at.text)
at.accept()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#collapseOne']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='text-box.php']").click()
time.sleep(2)


driver.quit()