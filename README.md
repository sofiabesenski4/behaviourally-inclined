## Learning how to use Python's BDD Tooling: _Behave_

```
import behave

```

# This is what the feature files look like:
```

Feature: showing off behave
# ~/features/tutorial.feature

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

```


```
# ~/features/steps/tutorial.py

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

```

