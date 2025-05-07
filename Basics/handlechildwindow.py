from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"div[class='float-right'] a:first-child").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
emailID = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print (emailID)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(emailID)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("hello")
driver.find_element(By.CSS_SELECTOR,"#terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait= WebDriverWait(driver,2)

errorGenerated = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[class ='alert alert-danger col-md-12']"))).text
assert errorGenerated == "Incorrect username/password."

