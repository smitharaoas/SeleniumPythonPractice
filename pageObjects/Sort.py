from selenium.webdriver.common.by import By

from Utils.Browser_Utils import BrowserUtils


class Sort(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.top_deals =(By.XPATH, "//a[text() ='Top Deals']")
        self.sort_icon = (By.XPATH, "//span[text() ='Veg/fruit name']")
        self.veggie_list = (By.CSS_SELECTOR, "tr td:first-child")
    def top_deals_click(self):
        self.driver.find_element(*self.top_deals).click()
    def switch_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
    def sort(self):
        self.driver.find_element(*self.sort_icon).click()
        elements = self.driver.find_elements(*self.veggie_list)
        web_sorted_list = []
        for ele in elements:
            web_sorted_list.append(ele.text)
        copied_veggies_list = web_sorted_list.copy()
        web_sorted_list.sort()
        assert copied_veggies_list == web_sorted_list
        print("sorted")