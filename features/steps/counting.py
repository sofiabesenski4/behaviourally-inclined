from behave import *
from hamcrest import assert_that, equal_to, is_not
# Must manually import the code under test in these steps.
import models 

# The context object trickles down through the steps, accumulating
# state which we prepare-act-assert on.
@given('a counter starting at {start}')
def step_impl(context, start):
    context.start = start
    context.counter = models.Incrementor(start = int(start)) 
    # Without the following line, the context.step_size variable persists between
    # the 
    """
  Given a counter starting at 0
  And with a step size of -1
  When we increment 1 time(s)
  Then we should see -1

  Given a counter starting at 0
  When we increment 2 time(s)
  Then we should see 2
    """
    #examples.
    context.step_size = context.counter.step_size

@given('with a step size of {step_size}')
def step_impl(context, step_size):
    context.step_size = step_size
    if context.counter:
        context.counter.step_size = int(step_size)
    else:
        context.counter = models.Incrementor(step_size = int(step_size))

@when('we increment {count} time(s)')
def step_impl(context, count):
    context.count = count
    context.counter.step(int(count))

@then('we should see {result}')
def step_impl(context, result):
    print(context.counter)
    expected_val = int(context.start) + int(context.step_size)*int(context.count)
    assert_that(int(context.counter.current), equal_to(expected_val))
