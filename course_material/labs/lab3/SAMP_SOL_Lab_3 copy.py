
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    is_less_than = False
    if number < cutoff:
        is_less_than = True
        print(f"{number} is less than {cutoff}")
    else:
        print(f"{number} is not less than {cutoff}")

    return is_less_than

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    return_val = "invalid"
    if type(decimal_number) == float:
        if decimal_number == 0:
            return_val = "zero"
        elif decimal_number > 0:
            return_val = "positive"
        else:
            return_val = "negative"

    return return_val

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    return_val = "invalid"
    if year >= 2001 and year <= 2100:
        return_val = "21st century"
    elif year >= 1901 and year <= 2000:
        return_val = "20th century"
    elif year >= 1801 and year <= 1900:
        return_val = "19th century"
    elif year < 1801:
        return_val = "ancient"

    return return_val

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    largest = None
    for num in [number_1, number_2, number_3]:
        if type(num) not in [int, float]:
            return None
    if number_1 > number_2 and number_1 > number_3:
        largest = number_1
    elif number_2 > number_1 and number_2 > number_3:
        largest = number_2
    else:
        largest = number_3
    
    return largest

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    return_val = "Invalid"
    if scale_used == "C":
        if temperature < 0:
            return_val = "Solid"
        elif temperature >= 100:
            return_val = "Gas"
        else:
            return_val = "Liquid"
    elif scale_used == "F":
        if temperature < 32:
            return_val = "Solid"
        elif temperature >= 212:
            return_val = "Gas"
        else:
            return_val = "Liquid"

    return return_val

