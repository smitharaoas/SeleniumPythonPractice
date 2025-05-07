from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Utils.Browser_Utils import BrowserUtils
from pageObjects.Confirmation import ConfirmationPage


class AddAddress(BrowserUtils):
    def __init__(self, driver,country_name):
        super().__init__(driver)
        self.driver = driver
        self.country_field = (By.CSS_SELECTOR, "#country")
        print(country_name)
        self.country_dropdown_select = (By.LINK_TEXT, country_name)
        self.accept_terms = (By.CSS_SELECTOR, "div[class*='checkbox']")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")

    def add_address(self,country_name):
        self.driver.find_element(*self.country_field).send_keys(country_name)
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(self.country_dropdown_select))
        self.driver.find_element(*self.country_dropdown_select).click()
        self.driver.find_element(*self.accept_terms).click()
        self.driver.find_element(*self.submit_button).click()
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page
