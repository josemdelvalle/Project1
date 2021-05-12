Feature: Project1 LogIn Works

  Scenario Outline:
    Given The User is on the Project 1 LogIn Page
    When The user types the <username> in the username bar
    And The user types the <password> in the password bar
    And Presses the submit button
    Then The Logged in <message> appears


    Examples:
      |username | password| message   |
      |Robert   |Stark    | Logged in |
      |Jose     |Del Valle| Logged in |
      |Alex     |Al       | Logged in |
      |Joe      |Williams | Logged in |