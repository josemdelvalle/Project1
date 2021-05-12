Feature: Project1 Reimbursement

  Scenario:
    Given The User is on the Project 1 LogIn Page
    And The user is Signed in
    And The user presses the courses tab
    When The user fills the form for a course
    And The user presses the submit course button
    Then The submitted record course appears
