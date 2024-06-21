import pytest
from pages.registration_page import RegistrationPage
from test_data.Registration_data import HomePageData
from utilities.tests_status import FinalTestStatus


@pytest.mark.usefixtures("setup")
class Test_Home:
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.registrationPage = RegistrationPage(self.driver)
        self.testStatus = FinalTestStatus()

    def test_registration(self,getData):
        self.registrationPage.registration(getData["firstname"], getData["email"], getData["dob"])
        result = self.registrationPage.verify_order("Success")
        self.testStatus.mark(result, "Order status")
        result2 = self.registrationPage.verify_registration_page_title("ProtoCommerce")
        self.testStatus.markFinal("test_registration", result2, "Title")

    @pytest.fixture(params=HomePageData.test_formSubmission)
    def getData(self, request):
        return request.param
