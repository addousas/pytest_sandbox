
from src.app.basic_math import BasicMath
import pytest

@pytest.mark.webtest
@pytest.mark.parametrize("param1, param2, results", [(1, 1, 1)])
def test_add():
    assert BasicMath().add(param1,param2) == results


def test_subtract():
    assert BasicMath().sub(2,2) == 2

def test_mult():
    assert BasicMath().mult(1,4) == 4


