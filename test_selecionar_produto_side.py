import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLoginetestedecompras():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.implicitly_wait(20)  
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginetestedecompras(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-price\"]").text == "$29.99"
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Products"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-badge\"]").text == "1"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"title\"]").text == "Your Cart"
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"item-quantity\"]").text == "1"
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-price\"]").text == "$29.99"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"logout-sidebar-link\"]").click()