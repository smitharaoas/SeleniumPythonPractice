import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(4)
mobile = "Blackberry"
countryNameSuggestion ="Ind"
countryName ="India"
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products = driver.find_elements(By.CSS_SELECTOR,"div[class ='card h-100']")
for product in products:
    productName = product.find_element(By.CSS_SELECTOR,"div h4").text
    if productName == mobile:
        product.find_element(By.CSS_SELECTOR,"div[class='card-footer'] button").click()
        print("Product added")
        break
driver.find_element(By.XPATH,"//a[contains(text(),'Checkout')]").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys(countryNameSuggestion)
country = (By.LINK_TEXT,"India")
WebDriverWait(driver,15).until(EC.visibility_of_element_located(country))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class*='checkbox']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successMsgCaptured = driver.find_element(By.CSS_SELECTOR,"div[class*='alert'] ").text
assert "Success" in successMsgCaptured




