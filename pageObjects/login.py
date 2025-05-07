from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from Utils.Browser_Utils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username =(By.CSS_SELECTOR, "#username")
        self.password = (By.CSS_SELECTOR, "#password")
        self.signin_button =(By.ID, "signInBtn")

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page
