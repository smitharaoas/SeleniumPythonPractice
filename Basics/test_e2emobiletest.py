import json

import pytest



from pageObjects.login import LoginPage
data_path = "../data/test_e2emobiletest.json"
with open(data_path) as f:
    test_data = json.load(f)
    test_data_list = test_data["data"]

@pytest.mark.parametrize("test_list",test_data_list)

@pytest.mark.smoke
def test_e2etest(browser_driver,test_list):
    driver=browser_driver
    print(driver)
    countryname="India"
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    print(test_list)
    login_page=LoginPage(driver)

    shop_page = login_page.login(test_list["username"],test_list["password"])
    # print(login_page.get_title())
    shop_page.add_to_cart(test_list["mobile"])
    # print(shop_page.get_title())
    checkout_page = shop_page.checkout()
    print("--"+checkout_page.get_title())
    add_address_page = checkout_page.check_out_page(countryname)

    # print(add_address_page.get_title())
    confirmation_page = add_address_page.add_address(countryname)
    print(confirmation_page.get_title())
    confirmation_page.confirmation()












