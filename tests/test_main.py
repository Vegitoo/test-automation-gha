from main import factorials
import pytest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_factorial_positive():
    result = list(factorials(5))
    assert result == [
        1,
        2,
        6,
        24,
        120,
    ], f"Expected [1, 2, 6, 24, 120], but got {result}"


def test_factorial_zero():
    result = list(factorials(0))
    assert result == [], f"Expected [], but got {result}"


def test_factorial_negative():
    with pytest.raises(ValueError):
        list(factorials(-5))


def test_factorial_fraction():
    with pytest.raises(TypeError):
        list(factorials(5.5))
