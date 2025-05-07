import time
from operator import contains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
driver.maximize_window()
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Practice").click()
time.sleep(5)
driver.find_element(By.ID,"name").send_keys("Smitha")
driver.find_element(By.ID,"email").send_keys("smitharao90@gmail.com")
driver.find_element(By.ID,"agreeTerms").click()
driver.find_element(By.ID,"form-submit").click()
wait = WebDriverWait(driver,5)
confoMsg = wait.until(ec.visibility_of_element_located((By.XPATH,"//h2[text() = 'Enter code here']"))).text
assert "Enter code here" in confoMsg
driver.switch_to.default_content()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()