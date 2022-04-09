Feature: showing off behave

  Scenario: Using the counter
     Given starting at 0 with a step size of 1 
      When we increment 1 time(s)
      Then we should see 1. 

     Given starting at 2 with a step size of 3
     When we increment 2 time(s)
     Then we should see 8


