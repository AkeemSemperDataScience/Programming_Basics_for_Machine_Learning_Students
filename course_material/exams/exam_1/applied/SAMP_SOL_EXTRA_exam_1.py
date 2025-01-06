import os

# Q1
# This function takes in two integers and returns the greatest common denominator between them
# The greatest common denominator is the largest integer that divides both numbers
# For example, the greatest common denominator between 12 and 18 is 6
def greatestCommonDenominator(a, b):
    i = 1
    gcd = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1
    return gcd
# Q2 
# This function takes in a data structure and returns a list of the unique characters in the data structure in alphabetical order
# The unique characters are the characters that appear, but we only want to include them once
# For example, if the data structure is "hello", the unique characters are ['h', 'e', 'l', 'o']
# If we sort the unique characters in alphabetical order, we get ['e', 'h', 'l', 'o']
def listUniqueChars(data_structure):
    unique_set = set()
    try:
        unique_set = data_structure.set()
    except:
        for item in data_structure:
            unique_set.add(item)

    unique_list = list(unique_set)
    unique_list.sort()
    return unique_list
# Q3
def filterLongWords(words, n):
    filteredWords = []
    for word in words:
        if len(word) > n:
            filteredWords.append(word)
    return filteredWords
#q4
def lastLetterAbbreviation(words):
    abbreviations = []
    for word in words:
        abbreviations.append(word[:-1])
    return abbreviations

def addCharToDict(overall_dict, currChar):
    if currChar in overall_dict:
        overall_dict[currChar] += 1
    else:
        overall_dict[currChar] = 1
    return overall_dict
#Q5
def fileReaderLetters(filepath):
    text_lines = os.readlines(filepath)
    overall_dict = dict()
    for currLine in text_lines:
        for currChar in currLine:
            lowerChar = currChar.lower()
            overall_dict = addCharToDict(overall_dict, lowerChar)
    return overall_dict
#Q3
# This function takes in a file path and a letter and returns a tuple that measures:
#   - The number of lines in that file that have more characters that are less than or equal to the letter supplied. 
#   - The number of lines in that file that have more characters that are greater than the letter supplied.
# The "more characters less/greater than" is defined by comparing the letter in the argument to each letter in the line, 
# and counting how many are less than or greater than the letter in the argument.
# For example, if the file has the following lines:
#   "apple"
#   "banana"
#   "cherry"
# Then beforeLetterCounter(file_path, "b") will return (1, 2) because:
#   - "apple" has 1 character less than or equal to "b", and 4 characters greater than "b", so it is "most upper".
#   - "banana" has 2 characters greater than "b", and 4 characters less than or equal to "b", so it is "most lower". 
#   - "cherry" has 6 characters greater than "b", and 0 characters less than or equal to "b", so it is "most upper".

def beforeLetterCounter(filepath, letter):
    with open(filepath, 'r') as file:
        text_lines = file.readlines()
    countLowerMost = 0
    countUpperMost = 0
    for currLine in text_lines:
        lowCount = 0
        highCount = 0
        for currChar in currLine:
            if currChar <= letter:
                lowCount += 1
            if currChar > letter:
                highCount += 1
        if lowCount > countLowerMost:
            countLowerMost += 1
        if highCount > countUpperMost:
            countUpperMost += 1
    return (countLowerMost, countUpperMost)
