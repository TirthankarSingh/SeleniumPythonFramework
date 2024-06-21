import time

import pytest

from pages.confirm_page import ConfirmPage
from pages.registration_page import RegistrationPage
from pages.checkout_page import CheckoutPage
from test_data.Registration_data import HomePageData
from utilities.tests_status import FinalTestStatus


@pytest.mark.usefixtures("setup")
class Test_E2E:
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.registrationPage = RegistrationPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)
        self.confirmPage = ConfirmPage(self.driver)
        self.testStatus = FinalTestStatus()

    def test_MobileOrder(self):
        self.registrationPage.clickShop()
        self.checkoutPage.Product_AddToCart("Blackberry")
        self.checkoutPage.click_Checkout()
        status = self.checkoutPage.verifyAddedProduct("Blackberry")
        self.testStatus.mark(status, "Product verification")
        self.checkoutPage.click_finalCheckout()
        self.confirmPage.search_and_Select_Country("India")
        self.confirmPage.check_TermsAndCondition()
        self.confirmPage.click_ConfirmButton()
        status2 = self.confirmPage.verify_Success_Msg("Thank you! Your order will be delivered in next few weeks")
        self.testStatus.markFinal("test_MobileOrder", status2, "verifying order placed")
