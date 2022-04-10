import pytest

from calc import Calculator

def test_addition():
	c = Calculator()
	assert c.add(1,2) == 3

def test_subtraction():
	c = Calculator()
	assert c.subtract(3,2) == 1