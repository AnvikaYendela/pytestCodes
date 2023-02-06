from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for login page locators"""

    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')


class ProductPageLocators(object):
    """A class for products page locators"""
    pass
