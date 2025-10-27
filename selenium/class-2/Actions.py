import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/droppable.php")
driver.implicitly_wait(10)
driver.maximize_window()

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(source, target).perform()
time.sleep(3)

driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")

button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary");
ActionChains(driver).context_click(button).perform()
time.sleep(2)
driver.find_element(By.TAG_NAME, "body").click()  # Click elsewhere to close context menu
time.sleep(2)

driver.quit()
