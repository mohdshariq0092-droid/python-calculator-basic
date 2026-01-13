import pytest
from calculator.basic import add, subtract


@pytest.mark.sanity
def test_add():
    assert add(2, 3) == 5


@pytest.mark.sanity
def test_subtract():
    assert subtract(5, 3) == 2
