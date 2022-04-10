import pytest
from models import Counter


@pytest.fixture
def multiplier():
    class Doubler:
        def __init__(self):
            pass

        def call(self, current, count=1):
            return current * 2

        def __repr__(self):
            return "A doubler!"

    return Doubler()


def test_counting_up():
    inc = Counter(start=1, step_size=2)
    assert inc.current == 1
    inc.step()
    assert inc.current == 3


def test_counting_down():
    inc = Counter(start=0, step_size=-1)
    inc.step()
    assert inc.current == -1


def test_with_a_provided_function(multiplier):
    inc = Counter(start=2, step_func=multiplier)
    assert inc.current == 2
    inc.step()
    assert inc.current == 4
