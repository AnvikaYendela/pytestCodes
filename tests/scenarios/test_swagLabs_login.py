import time

import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from pytestBDDDemo.tests.utils.constants import PASSWORD, SWAGLABS_URL, USERNAME
from pytestBDDDemo.tests.pages.loginPage import LoginPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    return driver


@scenario('../features/swaglabslogin.feature', 'Verify User navigated to products page after successful login')
def test_login():
    pass


@given('User loads the swag labs url')
def load_swagLabs_page(driver):
    driver.get('https://www.saucedemo.com/')


@given('User has username and password')
def user_credentials():
    print("swaglabs url:", SWAGLABS_URL)
    print("username", USERNAME)
    print("password", PASSWORD)


@when('User enters the username and password')
def enter_credentials(driver):
    driver.get(SWAGLABS_URL)
    loginpage = LoginPage(driver)
    loginpage.enter_credentials()


@when('User clicks on the login button')
def login(driver):
    loginpage = LoginPage(driver)
    loginpage.login()


@then('User should be logged in successfully')
def verify(driver):
    loginpage = LoginPage(driver)
    title = loginpage.get_title()
    time.sleep(10)
    assert title == 'Swag Labs'
status