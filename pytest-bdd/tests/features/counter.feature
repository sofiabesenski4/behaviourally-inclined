Feature: Counting

  Scenario: Using the counter
    Given a counter starting at 0 with a step size of 2
    When we increment 2 time(s)
    Then we should see 4

    Given a counter starting at 1 with a step size of 2
    When we increment 2 time(s)
    Then we should see 5

    Given a counter starting at 1 with a step size of -1
    When we increment 2 time(s)
    Then we should see -1
