
from pytestBDDDemo.tests.pages.loginPage import BasePage
from pytestBDDDemo.locators import locators
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):
    """Page contains methods to add products,clicking on cart button etc.."""

    def __int__(self, driver):
        self.driver = driver
        super.__init__(self.driver)

    def addProducts(self):
        """Method add the products to cart"""
        self.click(locator=locators.ProductPageLocators.bike_light)
        self.click(locator=locators.ProductPageLocators.sauce_labs)
        self.click(locator=locators.ProductPageLocators.cart)

    def add_to_cart(self):
        """Method allows user to click on cart button"""
        self.click(locator=locators.ProductPageLocators.cart)

    def add_products(self, items):
        """Method allows user to add product based on input"""
        txt = self.driver.find_elements(*locators.ProductPageLocators.products_path)
        for i in range(len(items)):
            if items[i] in txt[i].text:
                txt[i].find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    def remove_products(self):
        """Method allows user to remove products"""
        txt = self.driver.find_elements(*locators.ProductPageLocators.remove_product)
        for i in range(len(txt)):
                txt[i].click()

    def count_products(self):
        return len(self.driver.find_elements(*locators.ProductPageLocators.products))

    def search_product(self, items):
        """Method allows user to search for a product"""
        txt = self.driver.find_elements(*locators.ProductPageLocators.products)
        for i in range(5):
            if items in txt[i].text:
                return "found"
        return "not found"








