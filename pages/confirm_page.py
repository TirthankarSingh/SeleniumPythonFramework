from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import logging

from base.base_page import BaseClass
from utilities.custom_logger import Get_Logger


class ConfirmPage(BaseClass):
    Country_Search = (By.XPATH, "//input[@id='country']")
    # Country_India = (By.LINK_TEXT, 'India"]')
    Confirm_Checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    Confirm = (By.XPATH, '//input[@value="Purchase"]')
    Success_msg = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')

    log = Get_Logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def search_and_Select_Country(self, country):
        self.sendKeys(*ConfirmPage.Country_Search, country)
        Element = self.waitForElement(By.LINK_TEXT, country)
        Element.click()

    def check_TermsAndCondition(self):
        self.clickElement(*ConfirmPage.Confirm_Checkbox)

    def click_ConfirmButton(self):
        self.clickElement(*ConfirmPage.Confirm)

    def verify_Success_Msg(self, message):
        return self.verifyText(*ConfirmPage.Success_msg, message)
