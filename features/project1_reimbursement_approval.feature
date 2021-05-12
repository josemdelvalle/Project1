Feature: Reimbursement Approval

  Scenario:
    Given The User is logged in and in the courses tab
    When The user presses the get courses tab
    And The user approves the course
    Then The submitted record appears approved
