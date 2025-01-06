import pytest

def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb * 1024 * 1024 * 1024
    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    num_char = len(name)
    if num_char % 2 == 1:
        is_odd = True
    else:
        is_odd = False
    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    if input_number < len(input_string):
        character_at = input_string[input_number]

    return character_at
def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    # Open the file
    file = open(file_name, "r")
    # Read the lines
    lines = file.readlines()
    # Close the file
    file.close()
    # Loop through the lines
    for line in lines:
        # Try to convert the line to a number
        try:
            number = int(line)
            list_of_nums.append(number)
        except:
            # If it fails, ignore it
            pass

    return list_of_nums

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    # Create a dictionary to hold the counts
    counts = {}
    # Loop through the list
    for num in list_numbers:
        # If the number is not in the dictionary, add it
        if num not in counts:
            counts[num] = 0
        # Increment the count
        counts[num] += 1
    # Find the mode
    max_count = 0
    for key in counts:
        if counts[key] > max_count:
            max_count = counts[key]
            mode_of_list = key

    return mode_of_list

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

## Example of calling a function to test these... 

in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

print(lab1Question6(4, 3, 2, 1))
print(lab1Question6(0, 0, 0, 0))
print(lab1Question6(10, 5, 2, 1))
print(lab1Question6(1, 1, 1, 1))
print(lab1Question6(2, 0, 0, 5))