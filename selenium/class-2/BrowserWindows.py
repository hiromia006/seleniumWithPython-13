import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.firefox.service import Service

# Specify geckodriver path
service = Service("/snap/bin/geckodriver")

driver = webdriver.Firefox(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")
driver.maximize_window()

currentWindow = driver.current_window_handle
print("Current Window Handle: ", currentWindow)

driver.switch_to.new_window(WindowTypes.TAB)
driver.get("https://www.tutorialspoint.com/selenium/practice/new-tab-sample.php")
links=driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, " new Tab ", link.get_attribute("href"))
time.sleep(2)
driver.close()
driver.switch_to.window(currentWindow)
print("Back to original window")
time.sleep(2)

driver.switch_to.new_window(WindowTypes.WINDOW)
driver.get("https://www.tutorialspoint.com/selenium/practice/new-tab-sample.php")
links=driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, " new Window ", link.get_attribute("href"))
time.sleep(2)
driver.close()
driver.switch_to.window(currentWindow)
print("Back to original window")
time.sleep(2)


driver.quit()

