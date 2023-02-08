from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for login page locators"""

    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')


class ProductPageLocators(object):
    """A class for products page locators"""
    products = (By.CLASS_NAME, 'inventory_item_name')
    add_cart = (By.CSS_SELECTOR, 'button.btn.btn_primary.btn_small.btn_inventory')
    cart = (By.CSS_SELECTOR, 'a.shopping_cart_link')
    sauce_labs = (By.ID, 'add-to-cart-sauce-labs-backpack')
    bike_light = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    products_path = (By.XPATH, '//div[@class= "inventory_item_description"]')
    addCart_path = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    remove_product = (By.XPATH, '//button[contains(text(),"Remove")]')


class CartPageLocators(object):
    product_name = (By.XPATH, '//div[@class="cart_item_label"]/a')
    price = (By.CLASS_NAME, 'inventory_item_price')
    qty = (By.CLASS_NAME, 'cart_quantity')
    checkout = (By.ID, 'checkout')


class ChekoutInfoPageLocators(object):
    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    zip_code = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')
    error = (By.CSS_SELECTOR, 'h3[data-test="error"]')

class CheckoutOverviewPageLocators(object):
    finish_button = (By.ID, 'finish')
    successful_text = (By.CSS_SELECTOR, 'h2.complete-header')
    quantity = (By.CSS_SELECTOR, 'div.cart_item div.cart_quantity')
    total_price = (By.CSS_SELECTOR, 'div.summary_info div.summary_subtotal_label')




