import pytest

from pages.checkout_page import CheckoutPage
from pages.registration_page import RegistrationPage
from test_data.Products_data import ProductsData


@pytest.mark.usefixtures("setup")
class Test_Products:
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.registrationPage = RegistrationPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)

    def test_verify_product(self, getData):
        self.registrationPage.clickShop()
        products = self.checkoutPage.get_ProductName()
        l = []
        for product in products:
            phone = product.text
            l.append(phone)
        assert getData in l

    @pytest.fixture(params=ProductsData.test_products)
    def getData(self, request):
        return request.param
