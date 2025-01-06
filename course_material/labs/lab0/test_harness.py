import pytest
from START_Lab_0 import lab0Question1, lab0Question2, lab0Question3

# Test cases for lab0Question1
def test_lab0Question1_test_1():
    assert lab0Question1(2, 3) == 5
def test_lab0Question1_test_2():
    assert lab0Question1(-5, 10) == 5
def test_lab0Question1_test_3():
    assert lab0Question1(0, 0) == 0

# Test cases for lab0Question2
def test_lab0Question2_test_1():
    assert lab0Question2("Hello") == "H,o"
def test_lab0Question2_test_2():
    assert lab0Question2("Python") == "P,n"
def test_lab0Question2_test_3():
    assert lab0Question2("GitHub") == "G,b"

# Test cases for lab0Question3
def test_lab0Question3_test_1():
    assert lab0Question3("John Doe") == "Doe, John"
def test_lab0Question3_test_2():
    assert lab0Question3("Jane Smith") == "Smith, Jane"
def test_lab0Question3_test_3():
    assert lab0Question3("Alice Johnson") == "Johnson, Alice"