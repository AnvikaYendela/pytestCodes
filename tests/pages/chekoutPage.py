from pytestBDDDemo.tests.pages.loginPage import BasePage
from pytestBDDDemo.locators import locators
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    """Page contains methods to log in to application by entering valid username and password"""

    def __int__(self, driver):
        self.driver = driver
        super.__init__(self.driver)

    def checkout_address(self, first_name, last_name, zip_code):
        self.send_keys(first_name, locator=locators.ChekoutInfoPageLocators.first_name)
        self.send_keys(last_name, locator=locators.ChekoutInfoPageLocators.last_name)
        self.send_keys(zip_code, locator=locators.ChekoutInfoPageLocators.zip_code)
        self.click(locator=locators.ChekoutInfoPageLocators.continue_button)

    def get_mandatoryfields(self):
        return self.driver.find_element(*locators.ChekoutInfoPageLocators.error).text

    def continue_order(self):
        self.click(locator=locators.ChekoutInfoPageLocators.continue_button)

    def finish_order(self):
        self.click(locator=locators.CheckoutOverviewPageLocators.finish_button)

    def get_success_message(self):
        return self.driver.find_element(*locators.CheckoutOverviewPageLocators.successful_text).text

    def getProductsInfo(self):
        price = self.driver.find_elements(*locators.CartPageLocators.price)
        quantity = self.driver.find_elements(*locators.CartPageLocators.qty)
        product = self.driver.find_elements(*locators.CartPageLocators.product_name)
        product_list = []
        for i in range(2):
            list = []
            list.append(price[i].text)
            list.append(quantity[i].text)
            list.append(product[i].text)

            Details = {}
            Details[product[i].text] = list
            product_list.append(Details)

        return product_list



