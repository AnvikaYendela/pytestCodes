import pytest
from pytest_bdd import scenario, given
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    return driver

@scenario('../features/login.feature', 'Verify Login with valid user name and password')
def test_login():
    pass


@given('User load the twitter login page')
def load_twitter_page(driver):
    driver.get('https://twitter.com')
    c = 2+3
    assert c == 5

@given('User has username and password')
def user_credentials():
    c = 3-2
    assert c == 1






