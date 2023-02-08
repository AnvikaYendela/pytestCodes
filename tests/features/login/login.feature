Feature: login to swag labs application and place the order

  Scenario Outline: Verify User place the order by adding products to cart
    Given User loads the swag labs url
    And User has username and password
    When User enters the <username> and <password>
    And User clicks on the login button
    And User should be logged in successfully
    And User adds products to the cart clicks on the cart button
    And User clicks on checkout button
    And User enters the firstname, lastname, zip code , clicks on continue button
    And User clicks on finish order
    Then User should be placed order successfully

    Examples:
    | username | password |
    | standard_user | secret_sauce|


