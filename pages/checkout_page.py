import logging
import time
from selenium.webdriver.common.by import By

from base.base_page import BaseClass
from utilities.custom_logger import Get_Logger


class CheckoutPage(BaseClass):

    products = (By.XPATH, '//div[@class="card h-100"]/div/h4/a')
    product_AddToCart = (By.XPATH, '//button[@class="btn btn-info"]')
    checkout = (By.XPATH, "//*[@class='nav-link btn btn-primary']")
    final_checkout = (By.XPATH, "//*[@class='btn btn-success']")
    added_product = (By.XPATH, "//h4/a[@href]")

    log = Get_Logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_ProductName(self):
        return self.getElements(*CheckoutPage.products)

    def click_Checkout(self):
        self.clickElement(*CheckoutPage.checkout)

    def verifyAddedProduct(self, product_name):
        return self.verifyText(*CheckoutPage.added_product, product_name)

    def click_finalCheckout(self):
        self.clickElement(*CheckoutPage.final_checkout)

    def Product_AddToCart(self, mobile_name):
        products = self.get_ProductName()
        i = -1
        for product in products:
            i += 1
            phone = product.text
            self.log.debug("item matching: " + str(phone))
            if phone == mobile_name:
                add_buttons = self.getElements(*CheckoutPage.product_AddToCart)
                add_buttons[i].click()
                self.log.info("clicked successfully on" + mobile_name + " Add to cart")
