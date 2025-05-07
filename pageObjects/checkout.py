from selenium.webdriver.common.by import By

from Utils.Browser_Utils import BrowserUtils
from pageObjects.add_address import AddAddress


class Checkout(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout = (By.CSS_SELECTOR, "button[class*='btn-success']")
    def check_out_page(self,country_name):
        self.driver.find_element(*self.checkout).click()
        add_address_page = AddAddress(self.driver,country_name)
        return add_address_page