from behave import *
import models 

@given('starting at {start} with a step size of {step_size}')
def step_impl(context, start, step_size):
    context.start = start
    context.step_size = step_size
    context.counter = models.Incrementor(start = start, step_size = step_size) 

@when('we increment {count} time(s)')
def step_impl(context, count):
    context.count = count
    context.counter.step(int(count))

@then('we should see {result}')
def step_impl(context, result):
    assert int(context.counter.current) == int(context.start) + int(context.step_size)*int(context.count)