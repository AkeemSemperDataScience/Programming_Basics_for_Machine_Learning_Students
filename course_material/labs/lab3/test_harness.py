from START_Lab_3 import lab3Question1, lab3Question2, lab3Question3, lab3Question4, lab3Question5
#from SAMP_SOL_Lab_3 import lab3Question1, lab3Question2, lab3Question3, lab3Question4, lab3Question5

def test_lab3Question1_1():
    assert lab3Question1(5, 10) == True
def test_lab3Question1_2():
    assert lab3Question1(15, 10) == False
def test_lab3Question1_3():
    assert lab3Question1(0, 10) == True
 
def test_lab3Question2_1():
    assert lab3Question2(0) == "zero"
def test_lab3Question2_2():
    assert lab3Question2(5.5) == "positive"
def test_lab3Question2_3():
    assert lab3Question2(-10) == "negative"

def test_lab3Question3_1():
    assert lab3Question3(2021) == "21st century"
def test_lab3Question3_2():
    assert lab3Question3(1950) == "20th century"
def test_lab3Question3_3():
    assert lab3Question3(1850) == "19th century"
def test_lab3Question3_4():
    assert lab3Question3(1500) == "ancient"
def test_lab3Question3_5():
    assert lab3Question3(1909) == "20th century"

def test_lab3Question4_1():
    assert lab3Question4(5, 10, 15) == 15
def test_lab3Question4_2():
    assert lab3Question4(10, 5, 15) == 15
def test_lab3Question4_3():
    assert lab3Question4(10, 15, 5) == 15
def test_lab3Question4_4():
    assert lab3Question4("invalid", 10, 15) == None

def test_lab3Question5_1():
    assert lab3Question5(25, "C") == "Liquid"
def test_lab3Question5_2():
    assert lab3Question5(-10, "C") == "Solid"
def test_lab3Question5_3():
    assert lab3Question5(110, "C") == "Gas"
def test_lab3Question5_4():
    assert lab3Question5(75, "F") == "Liquid"
def test_lab3Question5_5():
    assert lab3Question5(10, "F") == "Solid"
def test_lab3Question5_6():
    assert lab3Question5(220, "F") == "Gas"