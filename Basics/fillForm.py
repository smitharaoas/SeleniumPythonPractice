import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//form-comp/div/form/div[1]/input[@name='name']").send_keys("thejas")
driver.find_element(By.NAME,"email").send_keys("smitharao90@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("smitha")
GenderValue = Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
print(GenderValue)
GenderValue.select_by_visible_text("Female")
driver.find_element(By.ID,"exampleCheck1").click()
#driver.find_element(By.ID,"exampleFormControlSelect1").
driver.find_element(By.ID,"inlineRadio2").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
saveMessage = driver.find_element(By.CLASS_NAME,"alert-success").text
print(saveMessage)
print("Success")
assert "Success" in saveMessage
print("Assert Successfull")
driver.find_element(By.XPATH,"//form-comp/div/h4/input[@name='name']").send_keys("Helloo")




time.sleep(2)