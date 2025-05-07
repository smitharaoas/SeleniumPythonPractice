from selenium.webdriver.common.by import By

from Utils.Browser_Utils import BrowserUtils
from pageObjects.checkout import Checkout


class ShopPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_tab = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products_list =(By.CSS_SELECTOR, "div[class ='card h-100']")
        self.checkout_btn = (By.XPATH, "//a[contains(text(),'Checkout')]")


    def add_to_cart(self,mobile):
        self.driver.find_element(*self.shop_tab).click()
        products = self.driver.find_elements(*self.products_list)
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, "div h4").text
            if product_name == mobile:
                product.find_element(By.CSS_SELECTOR, "div[class='card-footer'] button").click()
                print("Product added")
                break

    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
        checkout_page = Checkout(self.driver)
        return checkout_page