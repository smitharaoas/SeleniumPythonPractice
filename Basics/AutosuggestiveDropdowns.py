import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.CSS_SELECTOR,"input[id='autosuggest']").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
for country in countries:
    if country.text == "India":
        country.click()
        break
countrySelected = driver.find_element(By.CSS_SELECTOR,"#autosuggest")
assert countrySelected.get_attribute("value") == "India"