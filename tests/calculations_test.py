# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    radius = 0
    result = area_of_circle(radius)
    assert result == 0


def test_area_of_circle_negative_radius():
    """Test with a negative radius to raise ValueError."""
    radius = -1
    with pytest.raises(ValueError):
        area_of_circle(radius)


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    assert get_nth_fibonacci(0) == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    assert get_nth_fibonacci(1) == 1


def test_get_nth_fibonacci_two():
    """Test with n=2."""
    assert get_nth_fibonacci(2) == 1


def test_get_nth_fibonacci_three():
    """Test with n=3."""
    assert get_nth_fibonacci(3) == 2


def test_get_nth_fibonacci_five():
    """Test with n=5."""
    assert get_nth_fibonacci(5) == 5


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    assert get_nth_fibonacci(10) == 55


def test_get_nth_fibonacci_negative():
    """Test with a negative number to raise ValueError."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-1) 