import logging
import time
from selenium.webdriver.common.by import By

from base.base_page import BaseClass
from utilities.custom_logger import Get_Logger


class RegistrationPage(BaseClass):
    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    checkbox_Icecream = (By.ID, 'exampleCheck1')
    gender = (By.XPATH, '//select[@class="form-control"]')
    employment_status = (By.XPATH, '//input[@id="inlineRadio1"]')
    success_msg = (By.XPATH, "//*[@class='alert alert-success alert-dismissible']")
    submit = (By.XPATH, "//*[@type='submit']")
    DOB = (By.NAME, "bday")

    log = Get_Logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickShop(self):
        self.clickElement(*RegistrationPage.shop)

    def enterName(self, name):
        self.sendKeys(*RegistrationPage.name, name)

    def enterEmail(self, email):
        self.sendKeys(*RegistrationPage.email, email)

    def clickIcecream(self):
        self.clickElement(*RegistrationPage.checkbox_Icecream)

    def clickEmploymentStatus(self):
        self.clickElement(*RegistrationPage.employment_status)

    def enterDob(self, dob):
        self.sendKeys(*RegistrationPage.DOB, dob)

    def clickSubmit(self):
        self.clickElement(*RegistrationPage.submit)

    def getMessage(self):
        message = self.getText(*RegistrationPage.success_msg)
        return message

    def registration(self, name, email, dob):
        self.enterName(name)
        self.enterEmail(email)
        self.clickIcecream()
        self.clickEmploymentStatus()
        self.enterDob(dob)
        self.clickSubmit()

        # return self.getMessage()
    def verify_order(self, message):
        # self.getText(*RegistrationPage.success_msg)
        print(message)
        return self.verifyText(*RegistrationPage.success_msg, message)

    def verify_registration_page_title(self, title):
        return self.verifyTitle(title)
