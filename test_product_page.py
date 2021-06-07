#!/usr/bin/python3
from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
def test_guest_can_add_product_to_basket():
    browser.get('http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear')
    browser.implicitly_wait(5)
    el = browser.find_element_by_id('add_to_basket_form')
    el.click() 
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    time.sleep(3)



