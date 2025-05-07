import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
name ="Smitha"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
radios = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
for radio in radios:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected()
        break
assert driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR,"#hide-textbox").click()
assert not driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR,"#show-textbox").click()
assert driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText
alert.accept()
time.sleep(2)
