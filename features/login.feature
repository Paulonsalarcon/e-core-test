Feature: User Login

  Background:
    Given user navigates to Login Page

  Scenario: Successful login with valid credentials
    When user enters the username "demouser"
    And user enters the password "abc123"
    And user clicks in Login Button
    Then Invoice List Page must be open

  Scenario Outline: Unsuccessful login with invalid credentials
    When user enters the username "<username>"
    And user enters the password "<password>"
    And user clicks in Login Button
    Then error message 'Wrong username or password.' must be shown

    Examples:
      | username  | password |
      | Demouser  | abc123   | 
      | demouser_ | xyz      | 
      | demouser  | nananana |
      | demouser  | abc123   |