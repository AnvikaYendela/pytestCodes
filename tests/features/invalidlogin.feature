Feature: Invalid login page

Scenario: Verify User is navigated to product page after entering invalid credentials
    Given User loads the swag labs url
    And User has invalid username and password
    When User enters the invalid username and password
    And User clicks on the login button
    Then Displays error showing invalid credentials