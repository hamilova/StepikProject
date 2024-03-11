import time

import pytest
from selenium.webdriver.common.by import By

from pages.product_page import ProductPage
from pages.base_page import BasePage
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_item_to_cart()
#     product_page.solve_quiz_and_get_code()
#     # product_page.go_to_cart()
#     # product_page.check_item_in_cart()
#     product_page.item_added_in_cart_message()
#     # product_page.go_to_cart()
#     # product_page.check_product_name()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.is_not_element_present(By.CSS_SELECTOR, '.alertinner:first-of-type')

def test_guest_cant_see_success_message(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.is_not_element_present(By.CSS_SELECTOR, '.alertinner:first-of-type')

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.item_added_in_cart_message()
    product_page.is_disappeared(By.CSS_SELECTOR, '.alertinner:first-of-type')





