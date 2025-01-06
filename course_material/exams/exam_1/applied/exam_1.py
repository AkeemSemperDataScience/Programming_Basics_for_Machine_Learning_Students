import os

# These are pretty direct, there are no tricks or misdirection. If you're unsure or flustered, I'd reccomend:
#  - Define the problem - the inputs and output are specified, are you clear on those? 
#  - Write pseudocode to solve the problem. I think each challenge is something you can map out easily in English. 
#  - Attempt to translate the pseudocode into Python, step by step. If one step is too har or complex, it can likely be broken down further.
#  - If each step is relatively small/simple, you can look to documentation, examples to see how to do it. 
#       - E.g. if you need to get the variance of a bunch of numbers, you might not know the function, but you can look it up. 
#  - Making small tests here may be useful. 
# - If something doesn't work, use print/debugger/logging to check line by line what is changing, and that will identify the line where there is a mistake. 
#       - Build a test example where you knwo what should happen, and check to see where it goes wrong.
#
#
#
#
# Replace the "pass" with your code

# Q1
# This function takes in two integers and returns the greatest common denominator between them
# The greatest common denominator is the largest integer that divides both numbers
# For example, the greatest common denominator between 12 and 18 is 6
def greatestCommonDenominator(a, b):
    pass
# Q2 
# This function takes in a data structure and returns a list of the unique characters in the data structure in alphabetical order
# The unique characters are the characters that appear, but we only want to include them once
# For example, if the data structure is "hello", the unique characters are ['h', 'e', 'l', 'o']
# If we sort the unique characters in alphabetical order, we get ['e', 'h', 'l', 'o']
def listUniqueChars(data_structure):
    pass

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
    pass
