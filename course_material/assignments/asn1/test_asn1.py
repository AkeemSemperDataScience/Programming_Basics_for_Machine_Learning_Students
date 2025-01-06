import pytest
import START_asn_1
import math
import os

def toleranceEquals(a, b, tolerance):
    if math.isclose(a, b, abs_tol=tolerance):
        return True
    else:
        return False
FILE_1 = "Strength_Training.csv"
FILE_2 = "Car_Electronics.csv"
#FILE_1 = "https://github.com/AkeemSemper/Programming_Basics_for_ML/blob/5653d0473ae5d15ca092a31ef99dc68e8a1c1eb9/data/Strength%20Training.csv"
#FILE_2 = "https://github.com/AkeemSemper/Programming_Basics_for_ML/blob/c8545312b57f3b6a67b619ce732e0eaf1f064d73/data/Car%20Electronics.csv"

inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
inv_2 = START_asn_1.myInventory("Inv 2", FILE_2)

inv_1_item_1 = "Reebok Resistance Tube"
inv_1_item_1_init_rating = 4.4


def test_strengthLength():
    current_dir = os.getcwd()
    os.system(f"ls {current_dir}")
    real_val = 1097
    #inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
    stud_val = len(inv_1)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)

def test_strengthSubsetPrices():
    #inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
    real_val = 1020
    stud_val = inv_1.getPrices(5, 10000)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(len(stud_val), real_val, .01)

def test_strengthRating1():
    #inv_1 = START_asn_1.myInventory("Inv 1", FILE_1)
    stud_val = inv_1.itemRating(inv_1_item_1)
    real_val = inv_1_item_1_init_rating
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)

#def test_strengthRatingChange():
#    inv_1.addReviews(inv_1_item_1, 5, 50)

def test_carLength():
    #inv_2 = START_asn_1.myInventory("Inv 2", FILE_2)
    real_val = 976
    stud_val = len(inv_2)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)

def test_addInv():
    new_inv = inv_1 + inv_2
    real_val = 976+1097
    stud_val = len(new_inv)
    print("Student Value: ", stud_val, "Real Value: ", real_val)
    assert toleranceEquals(stud_val, real_val, .01)
