Feature: showing off behave

  Scenario: Using the counter
    Given a counter starting at 1
    And with a step size of 1
    When we increment 1 time(s)
    Then we should see 2

    Given a counter starting at 2
    And with a step size of 3
    When we increment 2 time(s)
    Then we should see 8

    Given a counter starting at 0
    When we increment 1 time(s)
    Then we should see 1

    Given a counter starting at 0
    When we increment 2 time(s)
    Then we should see 2
