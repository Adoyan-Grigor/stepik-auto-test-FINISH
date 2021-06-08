#!/usr/bin/python3
from selenium import webdriver
import pytest
import time
import math
browser = webdriver.Chrome()

@pytest.mark.parametrize('link', ["0", "1","2", "3", "4", "5", "6", "7", "8", "9"])

def test_guest_can_add_product_to_basket(browser, link):
    lk = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}")
    browser.get(lk)
    browser.implicitly_wait(5)
    el = browser.find_element_by_id('add_to_basket_form')
    el.click() 
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    time.sleep(1)
    browser.quit()





