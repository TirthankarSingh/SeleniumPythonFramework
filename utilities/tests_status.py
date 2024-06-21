import logging
from traceback import print_stack
from utilities.custom_logger import Get_Logger


class FinalTestStatus:
    log = Get_Logger(logging.INFO)

    def __init__(self):
        """
        Inits CheckPoint class
        """
        super().__init__()
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL ::  " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED ::  " + resultMessage)
                    # self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED ::  " + resultMessage)
                # self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            # self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName="default", result=None, resultMessage="No message given"):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
