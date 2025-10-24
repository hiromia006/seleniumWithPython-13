import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")
driver.maximize_window()

driver.switch_to.frame(0)
print("Frame 1 text box")
list = driver.find_elements(By.TAG_NAME, "a")
for item in list:
    print(item.text)
time.sleep(2)
# driver.switch_to.default_content()
driver.switch_to.parent_frame()

driver.find_element(By.CSS_SELECTOR, "button[data-bs-target='#collapseOne']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='text-box.php']").click()
time.sleep(2)

driver.quit()
