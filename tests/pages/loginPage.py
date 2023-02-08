from pytestBDDDemo.locators import locators
from pytestBDDDemo.tests.utils.constants import USERNAME, PASSWORD


class BasePage:
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, value, locator):
        """This method allows user to enter text in a field"""

        element = self.driver.find_element(*locator)
        element.send_keys(value)

    def get_text(self, locator):
        """This method allows user to get text in a field"""

        element = self.driver.find_element(*locator)
        element.text

    def click(self, locator):
        """This method allows user to perform click operation"""

        element = self.driver.find_element(*locator)
        element.click()


class LoginPage(BasePage):
    """Page contains methods to log in to application by entering valid username and password"""

    def __int__(self, driver):
        self.driver = driver
        super.__init__(self.driver)

    def enter_credentials(self, username, password):
        """Enter credentials like username and password"""

        self.send_keys(username, locator=locators.LoginPageLocators.user_name)
        self.send_keys(password, locator=locators.LoginPageLocators.password)

    def login(self):
        """Click on Login button"""

        self.click(locator=locators.LoginPageLocators.login_button)

    def get_title(self):
        """Get page title after successfully login"""

        return self.driver.title
