import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def browser():
    # Specify geckodriver path
    service = Service("/snap/bin/geckodriver")

    driver = webdriver.Firefox(service=service)
    driver.get("https://www.saucedemo.com/")

    driver.maximize_window()
    yield driver
    driver.quit()


def test_title(browser):
    assert browser.title == "Swag Labs"


def test_txt(browser):
    login_text = browser.find_element(By.CSS_SELECTOR, ".login_logo").text
    assert login_text == "Swag Labs"


def test_login(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    product_text = browser.find_element(By.XPATH, "//span[@class='title']").text
    assert product_text == "Products"


def test_add_to_cart(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # time.sleep(2)
    assert len(browser.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) >= 1


def test_add_to_cart_item(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # time.sleep(2)
    assert len(browser.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) >= 1
    browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
    assert len(browser.find_elements(By.XPATH, "//div[@class='inventory_item_name']")) >= 1


def test_checkout_item(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # time.sleep(2)
    assert len(browser.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) >= 1
    browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
    assert len(browser.find_elements(By.XPATH, "//div[@class='inventory_item_name']")) >= 1

    browser.find_element(By.ID, "checkout").click()
    browser.find_element(By.ID, "first-name").send_keys("John")
    browser.find_element(By.ID, "last-name").send_keys("Doe")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    browser.find_element(By.ID, "continue").click()
    browser.find_element(By.ID, "finish").click()

def test_logout(browser):
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    assert browser.find_element(By.ID, "logout_sidebar_link").is_displayed() == True
    browser.find_element(By.ID, "logout_sidebar_link").click()
    assert browser.find_element(By.ID, "login-button").is_displayed() == True
