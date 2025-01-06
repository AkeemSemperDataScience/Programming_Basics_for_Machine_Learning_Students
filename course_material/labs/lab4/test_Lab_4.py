import math
import pytest
from START_Lab_4 import lab4Question1, lab4Question2, lab4Question3, lab4Question4, lab4Question5

def test_lab4Question1_1():
    studVal = lab4Question1(1, 10)
    corrVal = 25
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert math.isclose(studVal, corrVal, rel_tol=.001)
def test_lab4Question1_2():
    studVal = lab4Question1(0, 5)
    corrVal = 4
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert math.isclose(studVal, corrVal, rel_tol=.001)
def test_lab4Question1_3():
    studVal = lab4Question1(10, 20)
    corrVal = 75
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert math.isclose(studVal, corrVal, rel_tol=.001)

def test_lab4Question2_1():
    assert lab4Question2("Hello World") == "H_ll_ W_rld"
def test_lab4Question2_2():
    assert lab4Question2("Python is awesome") == "Pyth_n _s _w_s_m_"
def test_lab4Question2_3():
    assert lab4Question2("I love programming") == "_ l_v_ pr_gr_mm_ng"

def test_lab4Question3_1():
    studVal = lab4Question3(1000, 0.05)
    corrVal = 23
    print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert math.isclose(studVal, corrVal, rel_tol=.1)
def test_lab4Question3_2():
    studVal = lab4Question3(500, 0.1)
    corrVal = 12
    print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert math.isclose(studVal, corrVal, rel_tol=.1)
def test_lab4Question3_3():
    studVal = lab4Question3(2000, 0.08)
    corrVal = 15
    print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert math.isclose(studVal, corrVal, rel_tol=.1)

def test_lab4Question4_1():
    assert lab4Question4(10) == [2, 3, 5, 7]
def test_lab4Question4_2():
    assert lab4Question4(20) == [2, 3, 5, 7, 11, 13, 17, 19]
def test_lab4Question4_3():
    assert lab4Question4(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_lab4Question5_1():
    assert lab4Question5([80, 90, 70, 60, 85], 75) == (3, 2)
def test_lab4Question5_2():
    studVal = lab4Question5([95, 85, 90, 80, 75], 80)
    corrVal = (4, 1)
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert studVal == corrVal
def test_lab4Question5_3():
    assert lab4Question5([70, 65, 75, 80, 90], 70) == (4, 1)