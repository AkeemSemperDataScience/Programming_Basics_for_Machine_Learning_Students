import math

def lab5Question1(height, weight):
    # take in a height and a weight
    # Return a tuple that contains the BMI and the BMI category
    # BMI = weight / height^2
    # BMI Categories:
    # Underweight: < 18.5
    # Normal: 18.5 - 24.9
    # Overweight: 25 - 29.9
    # Obese: 30 or greater
    category = ""
    bmi = weight / height**2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return (bmi, category)

def lab5Question2(file_to_read, lowerLimitString, upperLimitString):
    # Take in a file name, a lower limit string, and an upper limit string
    # Read the file and return a list of all lines in the file that are between the lower limit string and the upper limit string
    # Include the lower limit string and the upper limit string in the output
    # remove any leading or trailing whitespace from the lines, new lines, etc
    file_used = open(file_to_read, "r")
    lines = file_used.readlines()
    file_used.close()
    selectedLines = set()
    for line in lines:
        if line >= lowerLimitString and line <= upperLimitString:
            selectedLines.add(line.strip())
            #print(line)
    return selectedLines

def lab5Question3(phrase):
    # Take in a phrase
    # Return an acronym of the phrase, all capitalized
    # For example, "Random Access Memory" should return "RAM"
    # "Central Processing Unit" should return "CPU"
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


def lab5Question4(string1, string2, printAsWell=True):
    # Take in two strings, and a boolean to control printing. 
    # Return a tuple of sets - the first set with the characters that are in both strings, the second set with the characters that are in only one of the strings
    # If printAsWell is True, also print the characters that are in both strings and the characters that are in only one of the strings
    # Make the printing similar to the following:
    # "Characters in both strings: ", BUNCH OF CHARACTERS
    # "Characters in only one string: ", ANOTHER BUNCH OF CHARACTERS
    in_both = set()
    in_one = set()
    for char in string1:
        if char in string2:
            in_both.add(char)
        else:
            in_one.add(char)
    for char in string2:
        if char not in string1:
            in_one.add(char)

    if printAsWell:
        print("Characters in both strings: ", in_both)
        print("Characters in only one string: ", in_one)

    return (in_both, in_one)