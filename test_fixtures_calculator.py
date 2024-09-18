# test_calculator.py

import pytest
from calculator import add, subtract, divide

@pytest.fixture
def setup_data():
    return 10, 5

def test_add_with_fixture(setup_data):
    a, b = setup_data
    assert add(a, b) == 15

def test_subtract_with_fixture(setup_data):
    a, b = setup_data
    assert subtract(a, b) == 5
