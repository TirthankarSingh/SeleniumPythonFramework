from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *


class SeleniumDriver:

    def __init__(self, driver):
        # self.log = None
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getElement(self, by, value):
        element = None
        try:
            element = self.driver.find_element(by, value)
            self.log.info("Element found with locator::" + str(by) + " and value " + str(value))

        except Exception as e:
            self.log.error("element not found with locator::" + str(by) + " and value " + str(value))
            assert False
        return element

    def getElements(self, by, value):
        element = None
        try:
            elements = self.driver.find_elements(by, value)
            self.log.info("Element found with locator::" + str(by) + " and value " + str(value))
            self.log.info("Total Element found: " + str(len(elements)))

        except Exception as e:
            self.log.error("element not found with locator::" + str(by) + " and value " + str(value))
            assert False
        return elements

    def clickElement(self, by, value):
        try:
            element = self.getElement(by, value)
            element.click()
            self.log.info("Clicked on element with locator::" + str(by) + " and value " + str(value))
        except Exception as e:
            self.log.error("Cannot click on element with locator::" + str(by) + " and value " + str(value))
            assert False

    def sendKeys(self, by, value, text):
        try:
            element = self.getElement(by, value)
            element.send_keys(text)
            self.log.info("send data on element with locator type::" + str(by) + " and value " + str(value))
        except Exception as e:
            self.log.error("Cannot send data on element with locator::" + str(by) + " and value " + str(value))
            assert False
            # print_stack()

    def getText(self, by, value):
        message = None
        try:
            element = self.getElement(by, value)
            message = element.text
            self.log.info(
                "fetching text successfully on element with locator type::" + str(by) + " and value " + str(value))
            self.log.info("text:: " + message)
        except Exception as e:
            self.log.error(
                "fetching text unsuccessfull on element with locator::" + str(by) + " and value " + str(value))
            assert False
        return message

    def ElementPresentCheck(self, by, value):
        try:
            elementlist = self.driver.find_elements(by, value)
            if len(elementlist) > 0:
                self.log.info("Element found")
                return True
        except Exception as e:
            self.log.info("Element not found")
            return False

    def waitForElement(self, by, value, timeout=20, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for the element to be visible for::" + str(timeout) + " seconds")
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(expected_conditions.presence_of_element_located((by, value)))
            self.log.info("element appeared on webpage")
        except Exception as e:
            self.log.error("Element not appeared")
            assert False
        return element


