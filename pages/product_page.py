from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        item_link = self.browser.find_element(*ProductPageLocators.ADD_ITEM_TO_THE_BASKET_LINK)
        item_link.click()
        pass

    def go_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()
        pass

    def check_item_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_IN_BASKET), "Item is not presented"
        pass

    def item_added_in_cart_message(self):
        message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE)
        assert "has been added" in message.text


    def check_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        actual_name = product_name_element.text()
        expected_name = product_name_in_basket.text()
        assert actual_name == expected_name, f"Expected product name: '{expected_name}', Actual product name: '{actual_name}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_dissappear(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_MESSAGE), \
            "Success message is presented, but should not be"