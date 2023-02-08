import pytest
from pytest_bdd import given, when, parsers
from selenium import webdriver
from pytestBDDDemo.tests.pages.loginPage import LoginPage
import time
from pytestBDDDemo.tests.utils.constants import PASSWORD, SWAGLABS_URL, USERNAME


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    return driver


@given('User loads the swag labs url')
def load_swagLabs_page(driver):
    driver.get('https://www.saucedemo.com/')


@given('User has username and password')
def user_credentials():
    print("swaglabs url:", SWAGLABS_URL)
    print("username", USERNAME)
    print("password", PASSWORD)


@when(parsers.parse("User enters the {username} and {password}"))
def enter_credentials(driver, username, password):
    driver.get(SWAGLABS_URL)
    login_page = LoginPage(driver)
    login_page.enter_credentials(username, password)
    time.sleep(1)


@when('User clicks on the login button')
def login(driver):
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(1)


@when('User should be logged in successfully')
def verify(driver):
    loginpage = LoginPage(driver)
    title = loginpage.get_title()
    time.sleep(1)
    assert title == 'Swag Labs'
