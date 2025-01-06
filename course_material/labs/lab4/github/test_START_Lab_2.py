from START_Lab_2 import lab2Question1, lab2Question2, lab2Question3, lab2Question4, isValidPassword

def test_lab2Question1():
    assert lab2Question1("racecar") == True
    assert lab2Question1("hello") == False
    assert lab2Question1("madam") == True

def test_lab2Question2():
    assert lab2Question2(0) == []
    assert lab2Question2(1) == [0]
    assert lab2Question2(5) == [0, 1, 1, 2, 3]

def test_lab2Question3():
    assert lab2Question3("coding is cool", "co") == 2
    assert lab2Question3("hello world", "o") == 2
    assert lab2Question3("python is fun", "xyz") == 0

def test_lab2Question4():
    assert lab2Question4([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert lab2Question4([-1, 0, 1], [1, 0, -1]) == [0, 0, 0]
    assert lab2Question4([], []) == []

def test_isValidPassword():
    assert isValidPassword("Password123") == True
    assert isValidPassword("password") == False
    assert isValidPassword("12345678") == False