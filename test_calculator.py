# test_calculator.py
import pytest
from calculator import add, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0    

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(0, 0) == 0
    assert subtract(5, 10) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3        
    
    with pytest.raises(ValueError):
        divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 200, 300),
    (1e10, 1e10, 2e10)
])
def test_add(a, b, expected):
    assert add(a, b) == expected     


@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2),
    (5, 2, 2.5),
    (0, 5, 0)    
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected          