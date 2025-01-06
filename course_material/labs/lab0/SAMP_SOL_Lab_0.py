def lab0Question1(num1, num2):
    # Create a function that returns the sum of two numbers
    total = None
    total = num1 + num2

    return total

def lab0Question2(name):
    # Return the first and last character of the input string
    # return them as a string with a comma in between
    first_last = None
    first_last = name[0] + "," + name[-1]

    return first_last

def lab0Question3(full_name):
    # Return the incoming name (First Last) in the following format: Last, First
    last_first = None
    full_name = full_name.split()
    last_first = full_name[1] + ", " + full_name[0]

    return last_first
