
from pytestBDDDemo.tests.pages.loginPage import BasePage
from pytestBDDDemo.locators import locators
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):
    """Page contains methods to log in to application by entering valid username and password"""

    def __int__(self, driver):
        self.driver = driver
        super.__init__(self.driver)

    def addProducts(self):
        self.click(locator=locators.ProductPageLocators.bike_light)
        self.click(locator=locators.ProductPageLocators.sauce_labs)
        self.click(locator=locators.ProductPageLocators.cart)

    def add_to_cart(self):
        self.click(locator=locators.ProductPageLocators.cart)

    def add_products(self, items):
        txt = self.driver.find_elements(*locators.ProductPageLocators.products_path)
        for i in range(len(items)):
            if items[i] in txt[i].text:
                txt[i].find_element(By.XPATH, '//button[contains(text(),"Add to cart")]').click()

    def remove_products(self):
        txt = self.driver.find_elements(*locators.ProductPageLocators.remove_product)
        for i in range(len(txt)):
                txt[i].click()
        return len(self.driver.find_elements(*locators.ProductPageLocators.products))

    def search_product(self, items):
        txt = self.driver.find_elements(*locators.ProductPageLocators.products)
        for i in range(5):
            if items in txt[i].text:
                return "found"
        return "not found"








