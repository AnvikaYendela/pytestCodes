Feature: login to swag labs application
  Scenario: Verify User navigated to products page after successful login
    Given User loads the swag labs url
    And User has username and password
    When User enters the username and password
    And User clicks on the login button
    Then User should be logged in successfully

