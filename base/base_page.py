from base.selenium_driver import SeleniumDriver


class BaseClass(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyTitle(self, title_to_verify):

        actualTitle = self.getTitle()

        if actualTitle == title_to_verify:
            self.log.info("Title Verification Successful")
            return True
        else:
            self.log.error("Title Verification Failed")
            self.log.error("Actual Title: " + actualTitle + " Expected Title: " + title_to_verify)
            return False

    def verifyText(self, by, value, text):
        message = self.getText(by, value)
        if text in message:
            self.log.info("Text Verification Successful")
            return True
        else:
            self.log.error("Text Verification Failed")
            self.log.error("Actual Text: " + message + " Expected Text: " + text)
            return False



