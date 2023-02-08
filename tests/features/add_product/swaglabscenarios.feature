Feature: login to swag labs application and place the order

  Background:
    Given User loads the swag labs url

  Scenario Outline: Verify User not found any products after removing products from cart page
    Given User has username and password
    When User enters the <username> and <password>
    And User clicks on the login button
    And User should be logged in successfully
    And User adds products to the cart and click on cart button
    And User removes products from cart page
    Then User should found no products

    Examples:
    | username | password |
    | standard_user | secret_sauce|

  Scenario Outline: Verify error when searched product not found
    Given User has username and password
    When User enters the <username> and <password>
    And User clicks on the login button
    And User should be logged in successfully
    And User search for a product in products page
    Then User should see the error when searched product is not found

    Examples:
    | username | password |
    | standard_user | secret_sauce|

  Scenario Outline: Verify user not proceed to checkout page without entering address details
    Given User has username and password
    When User enters the <username> and <password>
    And User clicks on the login button
    And User should be logged in successfully
    And User adds products to the cart and click on cart button
    And User clicks on checkout button and clicks on finish button
    Then User should not proceed to checkout page

  Examples:
    | username | password |
    | standard_user | secret_sauce|

