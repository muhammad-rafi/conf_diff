import pytest


@pytest.mark.parametrize("a,b,c", [(10, 20, 30)])
def test_addition(a, b, c):
    assert a + b == c


@pytest.mark.parametrize("x,y,z", [(40, 30, 10)])
def test_substraction(x, y, z):
    assert x - y == z
