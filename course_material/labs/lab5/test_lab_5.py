import pytest
import math
import os
try:
    from START_Lab_5 import lab5Question1, lab5Question2, lab5Question3, lab5Question4
except:
    from SAMP_SOL_Lab_5 import lab5Question1, lab5Question2, lab5Question3, lab5Question4

def test_lab5Question1_1():
    studVal = lab5Question1(1.8, 80)
    corrVal = (24.69, "Normal")
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    bmiClose = math.isclose(studVal[0], corrVal[0], rel_tol=.1)
    catMatch = studVal[1] == corrVal[1]
    assert bmiClose and catMatch
def test_lab5Question1_2():
    studVal = lab5Question1(1.8, 102)
    corrVal = (31.5, "Obese")
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    bmiClose = math.isclose(studVal[0], corrVal[0], rel_tol=.1)
    catMatch = studVal[1] == corrVal[1]
    assert bmiClose and catMatch
def test_lab5Question1_3():
    studVal = lab5Question1(1.7, 50)
    corrVal = (17.3, "Underweight")
    #print("Student Value: ", studVal, " Correct Value: ", corrVal)
    bmiClose = math.isclose(studVal[0], corrVal[0], rel_tol=.1)
    catMatch = studVal[1] == corrVal[1]
    assert bmiClose and catMatch

# Question 2
filename = "course_material/labs/lab5/Lab5_input.txt"
try:
    if not os.path.exists(filename):
        filename = "Lab5_input.txt"
        print("Local file used")
except:
    print("Long path, using local file")
    pass
def test_lab5Question2_1():
    lowerLimit = "a"
    upperLimit = "z"
    studVal = lab5Question2(filename, lowerLimit, upperLimit)
    corrVal = set(['aspiration', 'classified', 'federation', 'graduation', 'millennium', 'philosophy', 'quadratics', 'transcript', 'wilderness'])
    print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert studVal == corrVal
def test_lab5Question2_2():
    lowerLimit = "b"
    upperLimit = "y"
    studVal = lab5Question2(filename, lowerLimit, upperLimit)
    corrVal = {'graduation', 'federation', 'transcript', 'millennium', 'wilderness', 'philosophy', 'classified', 'quadratics'}
    print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert studVal == corrVal
def test_lab5Question2_3():
    lowerLimit = "c"
    upperLimit = "x"
    studVal = lab5Question2(filename, lowerLimit, upperLimit)
    corrVal = {'graduation', 'federation', 'transcript', 'millennium', 'wilderness', 'philosophy', 'classified', 'quadratics'}
    print("Student Value: ", studVal, " Correct Value: ", corrVal)
    assert studVal == corrVal

# Question 3
def test_lab5Question3_1():
    inputPhrase = "Random Access Memory"
    studVal = lab5Question3(inputPhrase)
    corrVal = "RAM"
    assert studVal == corrVal
def test_lab5Question3_2():
    inputPhrase = "WuTang is for the children"
    studVal = lab5Question3(inputPhrase)
    corrVal = "WIFTC"
    assert studVal == corrVal
def test_lab5Question3_3():
    inputPhrase = "Where in the world is Carmen Sandiego"
    studVal = lab5Question3(inputPhrase)
    corrVal = "WITWICS"
    assert studVal == corrVal

# Question 4
def test_lab5Question4_1():
    string1 = "Hello"
    string2 = "World"
    studVal = lab5Question4(string1, string2, False)
    corrVal = ({'l', 'o'}, {'H', 'e', 'W', 'r', 'd'})
    assert studVal == corrVal
def test_lab5Question4_2():
    string1 = "Muchausen"
    string2 = "Syndrome"
    studVal = lab5Question4(string1, string2, False)
    corrVal = ({'e', 'n'}, {'M', 'u', 'c', 'h', 'a', 'y', 'd', 'o', 'm', 'r', 's', 'S'})
    assert studVal == corrVal
def test_lab5Question4_3():
    string1 = "Purple"
    string2 = "Haze"
    studVal = lab5Question4(string1, string2, False)
    corrVal = ({'e'}, {'P', 'u', 'r', 'p', 'l', 'H', 'a', 'z'})
    assert studVal == corrVal