import START_Lab_2
import pytest

q1_corr_1 = False
q1_corr_2 = True
q1_corr_3 = False

q2_corr_1 = [0, 1, 1, 2, 3, 5]
q2_corr_2 = [0, 1, 1, 2, 3, 5, 8]
q2_corr_3 = []

q3_corr_1 = 2
q3_corr_2 = 1
q3_corr_3 = 2

q4_corr_1 = [6.0, 8.0, 10.0, 12.0]
q4_corr_2 = []
q4_corr_3 = [5.0, 7.0, 14.0, 10.0]

q5_corr_1 = False
q5_corr_2 = True
q5_corr_3 = False

def test_lab2Question1_1():
    assert START_Lab_2.lab2Question1("purple") == q1_corr_1
def test_lab2Question1_2():
    assert START_Lab_2.lab2Question1("ada") == q1_corr_2
def test_lab2Question1_3():
    assert START_Lab_2.lab2Question1("hello") == q1_corr_3

def test_lab2Question2_1():
    assert START_Lab_2.lab2Question2(7) == q2_corr_1
def test_lab2Question2_2():    
    assert START_Lab_2.lab2Question2(12) == q2_corr_2
def test_lab2Question2_3():
    assert START_Lab_2.lab2Question2(-5) == q2_corr_3

def test_lab2Question3_1():
    assert START_Lab_2.lab2Question3("Coding is cool", "co") == q3_corr_1
def test_lab2Question3_2():
    assert START_Lab_2.lab2Question3("Attitude is everything", "tt") == q3_corr_2
def test_lab2Question3_3():
    assert START_Lab_2.lab2Question3("Superstitious and superfluous", "super") == q3_corr_3

def test_lab2Question4_1():
    assert START_Lab_2.lab2Question4([1, 2, 3, 4], [5, 6, 7, 8]) == q4_corr_1
def test_lab2Question4_2():
    assert START_Lab_2.lab2Question4([0, 0, 0, 0], [0, 0, 0]) == q4_corr_2
def test_lab2Question4_3():
    assert START_Lab_2.lab2Question4([1, 2, 8, 3], [4, 5, 6, 7]) == q4_corr_3

def test_isValidPassword_1():
    assert START_Lab_2.isValidPassword("password") == q5_corr_1
def test_isValidPassword_2():
    assert START_Lab_2.isValidPassword("Password1") == q5_corr_2
def test_isValidPassword_3():
    assert START_Lab_2.isValidPassword("12345678") == q5_corr_3