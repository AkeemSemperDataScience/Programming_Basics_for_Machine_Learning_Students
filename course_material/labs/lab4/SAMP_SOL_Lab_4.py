import math
import pytest
def lab4Question1(lower, upper):
    # take in two integers lower and upper
    # return the sum of all odd numbers between lower and upper (inclusive of lower, exclusive of upper)
    total = 0
    for i in range(lower, upper):
        if i%2 == 1:
            total += i
    return total

def lab4Question2(text):
    # take in a string
    # return the string with all the vowels (either case) replaced by underscores
    vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
    for char in text:
        if char in vowels:
            text = text.replace(char, "_")
    return text

def lab4Question3(money_value, interest_rate):
    # Take in a number that represents a money value, and a decimal number that represents an interest rate
    # E.g. .07 is 7% interest
    # Return the number of years that it will take for the money value to triple at the given interest rate
    # Return None if things are invalid - e.g. negative money value, negative interest rate, interest rate >= 1
    high_cutoff = float(money_value) * 3
    years = 0

    if interest_rate <= 0:
        return None
    if money_value <= 0:
        return None
    if interest_rate >= 1:
        return None

    while money_value < high_cutoff:
        money_value += money_value * float(interest_rate)
        years += 1
        #print("Year: ", years, " Money: ", money_value, " High Cutoff: ", high_cutoff)

    return int(math.ceil(years))

def lab4Question4(upper_limit):
    # take in a number that is an upper limit. 
    # return a list of all prime numbers up to that limit
    primes = []
    for num in range(2, upper_limit):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def lab4Question5(list_of_grades, passing_grade):
    # take in a list of numbers that represent grades between 0 and 100, and a number that represents the passing grade (also between 0 and 100)
    # return a tuple with the number of passing grades and the number of failing grades
    passing = 0
    failing = 0
    for grade in list_of_grades:
        if int(grade) >= int(passing_grade):
            passing += 1
            print("Grade: ", grade, " Passing Grade: ", passing_grade, " Passing: ", passing)
        else:
            failing += 1
            print("Grade: ", grade, " Passing Grade: ", passing_grade, " Failing: ", failing)
    return (passing, failing)

