from pytestBDDDemo.tests.pages.loginPage import BasePage
from pytestBDDDemo.locators import locators


class CartPage(BasePage):
    """Page contains methods to get product lists"""

    def __int__(self, driver):
        self.driver = driver
        super.__init__(self.driver)

    def getProducts(self):
        """Method returns the products list from cart page"""
        price = self.driver.find_elements(*locators.CartPageLocators.price)
        qty = self.driver.find_elements(*locators.CartPageLocators.qty)
        product = self.driver.find_elements(*locators.CartPageLocators.product_name)
        product_list = []
        for i in range(2):
            list = []
            list.append(price[i].text)
            list.append(qty[i].text)
            list.append(product[i].text)

            Details = {}
            Details[product[i].text] = list
            product_list.append(Details)

        return product_list

    def check_out(self):
        """Method click on checkout button"""
        self.click(locator=locators.CartPageLocators.checkout)
