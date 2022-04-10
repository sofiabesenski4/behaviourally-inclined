import pytest
from pytest_bdd import scenario, given, when, then, parsers
import models

# Scenarios


@scenario('../features/counter.feature', "Using the counter")
def test_counter():
    print("end of counting test")
    pass


# Given Steps
@given(parsers.parse('a counter starting at {start:d} \
    with a step size of {step_size:d}'))
def a_counter_starting_at(start, step_size):
    pytest.counter = models.Counter(start=start, step_size=step_size)


# When Steps
@when(parsers.parse('we increment {count:d} time(s)'))
def we_increment_a_number_of_times(count):
    pytest.counter.step(count)


# Then Steps
@then(parsers.parse('we should see {result:d}'))
def count_should_be(result):
    print("here")
    assert(int(pytest.counter.current) == result)
