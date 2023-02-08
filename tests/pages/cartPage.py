from pytestBDDDemo.tests.pages.loginPage import BasePage
from pytestBDDDemo.locators import locators


class CartPage(BasePage):
    """Page contains methods to log in to application by entering valid username and password"""

    def __int__(self, driver):
        self.driver = driver
        super.__init__(self.driver)

    def getProducts(self):
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
        self.click(locator=locators.CartPageLocators.checkout)