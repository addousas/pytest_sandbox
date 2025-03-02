
import pytest

test_data = [(1,2,3), (1,4,6), (4,5,9)]

@pytest.mark.parametrize("a,b,expected", test_data)
def test_add(math_unit, a, b, expected):
    assert math_unit.add(a,b) == expected

@pytest.mark.parametrize("a,b,expected", test_data)
def test_subtract(math_unit, a,b, expected):
    assert math_unit.sub(a,b) == expected

@pytest.mark.parametrize("a,b,expected", test_data)
def test_mult(math_unit, a,b, expected):
    assert math_unit.mult(a,b) == expected

@pytest.mark.parametrize("a,b,expected", test_data)
def test_div(math_unit, a,b, expected):
    assert math_unit.div(a,b) == expected



