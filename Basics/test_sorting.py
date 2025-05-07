import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Sort import Sort

def test_sort(browser_driver):
        driver = browser_driver
        print(driver)
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        sort = Sort(driver)
        print(sort.get_title())
        sort.top_deals_click()
        sort.switch_tab()
        print(sort.get_title())
        sort.sort()



