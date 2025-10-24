import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")
wait=WebDriverWait(driver,10)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "button[onclick='showAlert()']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()


driver.find_element(By.CSS_SELECTOR,"button[onclick='myDesk()']").click()
driver.switch_to.alert.dismiss()

# Optimize code
driver.find_element(By.XPATH, "//button[@onclick='myPromp()']").click()
at=driver.switch_to.alert
at.send_keys("Selenium Alert Prompt")
print(at.text)
at.accept()


driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#collapseOne']").click()
driver.find_element(By.XPATH, "//a[@href='text-box.php']").click()



driver.quit()