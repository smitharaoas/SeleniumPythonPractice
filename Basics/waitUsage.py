from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ber")
filteredProducts = driver.find_elements(By.CSS_SELECTOR,"div[class='product'] ")
assert len(filteredProducts) > 0
filteredProductsList =["Cucumber","Raspberry","Strawberry"]
filteredProductsListUI =[]

for products in filteredProducts:
    variable = products.find_element(By.CSS_SELECTOR,"h4[class='product-name']").text
    filteredProductsListUI.append(variable.split(" ")[0])
    products.find_element(By.CSS_SELECTOR,"div button").click()
print(filteredProductsListUI)
assert filteredProductsListUI == filteredProductsList
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
unitPrice = driver.find_elements(By.CSS_SELECTOR,"td:nth-child(5) p")
sumPrice = 0
for price in unitPrice:
    sumPrice = sumPrice + int(price.text)
totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sumPrice == totalAmount
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span[class='promoInfo']")))
codeAppliedText = driver.find_element(By.CSS_SELECTOR,"span[class='promoInfo']").text
assert "Code applied" in codeAppliedText
totalAfterDiscount = 0
if driver.find_element(By.CSS_SELECTOR,"span[class='promoInfo']").is_displayed():
    totalAfterDiscount = sumPrice - 0.1*sumPrice

totalAfterDiscountUI = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAfterDiscount == totalAfterDiscountUI

assert totalAmount > totalAfterDiscountUI

