from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,"Register here").click()
driver.find_element(By.CSS_SELECTOR,"#firstName").send_keys("Smitha")
driver.find_element(By.CSS_SELECTOR,"#lastName").send_keys("Rao")
driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("smitharao90@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userMobile").send_keys("8867534226")
driver.find_element(By.CSS_SELECTOR,"input[value='Female']").click()
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("SMITHA")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("SMITHA")
driver.find_element(By.CSS_SELECTOR,"input[formcontrolname='required']").click()
driver.find_element(By.CSS_SELECTOR,"#login").click()