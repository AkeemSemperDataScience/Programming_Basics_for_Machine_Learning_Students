def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    is_palindrome = False
    if word == word[::-1]:
        is_palindrome = True

    return is_palindrome

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    fib_sequence = []
    a, b = 0, 1
    while a < number_val:
        fib_sequence.append(a)
        a, b = b, a+b
    return fib_sequence

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    num_times = 0
    for i in range(len(str1)):
        if (str1[i:i+len(str2)] == str2) or (str1[i:i+len(str2)].lower() == str2.lower()):
            num_times += 1
    return num_times

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    sum_list = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            val_1 = float(list1[i])
            val_2 = float(list2[i])
            if val_1 == None:
                val_1 = 0
            if val_2 == None:
                val_2 = 0
            sum_list.append(val_1 + val_2)

    return sum_list

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None

    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    is_valid = False
    if len(password) >= 8:
        if any(char.isupper() for char in password):
            if any(char.islower() for char in password):
                if any(char.isdigit() for char in password):
                    is_valid = True

    return is_valid

