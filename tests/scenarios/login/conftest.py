import pytest
from pytest_bdd import scenario, given, when, then, scenarios, parsers
from selenium.webdriver.chrome import webdriver

from pytestBDDDemo.tests.pages.products import ProductsPage
from pytestBDDDemo.tests.utils.constants import PASSWORD, SWAGLABS_URL, USERNAME, SAUCE_LABS_BIKE, SAUCE_LABS_BACKPACK
from pytestBDDDemo.tests.pages.loginPage import LoginPage
import time


