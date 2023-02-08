import pytest
from pytest_bdd import when, then, parsers
from pytestBDDDemo.tests.utils.constants import FIRSTNAME, LASTNAME, ZIP, \
    SAUCE_LABS_BIKE, SAUCE_LABS_BACKPACK, ITEMS, PRODUCTNAME, ERROR
import time
from pytestBDDDemo.tests.pages.cartPage import CartPage
from pytestBDDDemo.tests.pages.chekoutPage import CheckoutPage
from pytestBDDDemo.tests.pages.products import ProductsPage


@pytest.fixture
def context():
    return {}


@when(parsers.parse("User adds products to the cart clicks on the cart button"))
def add_products(driver):
    products_page = ProductsPage(driver)
    products_page.addProducts()
    cart_page = CartPage(driver)
    products_list = cart_page.getProducts()
    for x in products_list:
        for values in x.values():
            print(values)
            if SAUCE_LABS_BIKE == values:
                assert values == SAUCE_LABS_BIKE
            else:
                assert values == SAUCE_LABS_BACKPACK
    time.sleep(1)


@when('User adds products to the cart, click on cart button')
def add_products(driver):
    products_page = ProductsPage(driver)
    products_page.add_products(ITEMS)
    products_page.add_to_cart()
    time.sleep(1)


@when('User search for a product in products page')
def search_products(driver, context):
    products_page = ProductsPage(driver)
    context = products_page.search_product(PRODUCTNAME)
    time.sleep(1)
    print(context)
    return context


@when('User clicks on checkout button , clicks on finish button')
def check_finish(driver):
    cartPage = CartPage(driver)
    cartPage.check_out()
    time.sleep(1)

    checkout_page = CheckoutPage(driver)
    checkout_page.continue_order()
    time.sleep(1)


@then('User should not proceed to checkout page')
def mandatory_fields(driver):
    checkout_page = CheckoutPage(driver)
    error_text = checkout_page.get_mandatoryfields()
    time.sleep(1)
    assert error_text == ERROR


@then('User should see the error when searched product is not found')
def search_results(context):
    print(context)
    if context == "not found":
        print("No results found")
    else:
        print("Results found")


@when('User clicks on checkout button')
def checkout(driver):
    cartPage = CartPage(driver)
    cartPage.check_out()
    time.sleep(1)


@when('User enters the firstname, lastname, zip code , clicks on continue button')
def add_address(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.checkout_address(FIRSTNAME, LASTNAME, ZIP)
    time.sleep(1)


@when('User clicks on finish order')
def finish(driver):
    checkout_page = CheckoutPage(driver)
    get_product_info = checkout_page.getProductsInfo()
    total_sum = float(SAUCE_LABS_BIKE[0].replace('$', '')) + float(SAUCE_LABS_BACKPACK[0].replace('$', ''))
    total_budget = 0
    for x in get_product_info:
        for values in x.values():
            sum += float(values[0].replace('$', ''))
            if SAUCE_LABS_BIKE == values:
                assert values == SAUCE_LABS_BIKE
            else:
                assert values == SAUCE_LABS_BACKPACK
    time.sleep(1)
    assert total_budget == total_sum


@then('User should be placed order successfully')
def order_placed(driver):
    checkout_page = CheckoutPage(driver)
    time.sleep(1)
    checkout_page.finish_order()
    time.sleep(1)
    assert checkout_page.get_success_message() == "THANK YOU FOR YOUR ORDER"


@then('User removes products from cart page')
def removed_products(driver):
    products_page = ProductsPage(driver)
    product_count = products_page.remove_products()
    time.sleep(1)
    assert product_count == 0
