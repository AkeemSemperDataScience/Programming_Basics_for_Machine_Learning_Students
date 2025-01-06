import exam_1
import math

file_name = "sample_text.txt"
tolerance = .01

def toleranceEquals(a, b, tolerance):
    if math.isclose(a, b, abs_tol=tolerance):
        return True
    else:
        return False

def test_q1test1():
    stud_val = exam_1.greatestCommonDenominator(97, 13)
    real_val = 1
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, tolerance)

def test_q1test2():
    stud_val = exam_1.greatestCommonDenominator(97, 97)
    real_val = 97
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, tolerance)

def test_q1test3():
    stud_val = exam_1.greatestCommonDenominator(239843120, 12)
    real_val = 4
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, tolerance)

def test_q1test4():
    stud_val = exam_1.greatestCommonDenominator(25, 90)
    real_val = 5
    assert toleranceEquals(stud_val, real_val, tolerance)

def test_q1test5():
    stud_val = exam_1.greatestCommonDenominator(120, 90)
    real_val = 30
    assert toleranceEquals(stud_val, real_val, tolerance)

def test_q2test1():
    stud_val = exam_1.listUniqueChars("asdkljf;asldfjsdfijapoijfasdkjflasdhfauiewhfr")
    real_val = ['a', 's', 'd', 'k', 'l', 'j', 'f', ';', 'i', 'o', 'p', 'h', 'u', 'e', 'w', 'r']
    real_val.sort()
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert stud_val == real_val

def test_q2test2():
    stud_val = exam_1.listUniqueChars("abcdefghijkllllllmnopqrstuvwxz")
    real_val = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
    real_val.sort()
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert stud_val == real_val

def test_q2test3():
    stud_val = exam_1.listUniqueChars("a")
    real_val = ['a']
    assert stud_val == real_val

def test_q3test1():
    real_val = (12, 100)
    stud_val = exam_1.beforeLetterCounter(file_name, "a")
    assert stud_val == real_val

def test_q3test2():
    real_val = (100, 55)
    stud_val = exam_1.beforeLetterCounter(file_name, "r")
    assert stud_val == real_val

def test_q3test3():
    real_val = (83, 80)
    stud_val = exam_1.beforeLetterCounter(file_name, "m")
    assert stud_val == real_val

def test_q3test4():
    real_val = (100, 0)
    stud_val = exam_1.beforeLetterCounter(file_name, "z")
    assert stud_val == real_val
