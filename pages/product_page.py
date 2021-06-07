import time

from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def should_be_product_added_to_cart(self):
        self.should_be_message()
        self.should_be_product_title_in_meessage()
        self.should_be_message_cart_price()
        self.should_be_cart_price()
        self.add_product_to_cart()


    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_message_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE_MESSAGE), "Cart price message not appear"

    def should_be_cart_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = product_price.text
        assert price in self.browser.find_element(*ProductPageLocators.CART_PRICE).text, "Price not match"

    def should_be_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Product added message not appear"

    def should_be_product_title_in_meessage(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        title = product_title.text
        assert title in self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text, "Product title in message not correct or missed"




