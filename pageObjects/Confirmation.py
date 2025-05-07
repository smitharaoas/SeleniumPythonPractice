from selenium.webdriver.common.by import By

from Utils.Browser_Utils import BrowserUtils


class ConfirmationPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.message_captured = (By.CSS_SELECTOR, "div[class*='alert'] ")

    def confirmation(self):
        success_msg_captured = self.driver.find_element(*self.message_captured).text
        assert "Success" in success_msg_captured