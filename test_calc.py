import pytest

from calc import Calculator

def test_addition():
	c = Calculator()
	assert c.add(1,2) == 3

def test_subtraction():
	c = Calculator()
	assert c.subtract(3,2) == 1

def test_multiplication():
	c = Calculator()
	assert c.multiply(2,3) == 6

def test_multiplication_two():
	c = Calculator()
	assert c.multiply(3,3) == 9

def test_division():
	c = Calculator()
	assert c.divide(6,2) == 3
