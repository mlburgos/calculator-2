def add(num_list):
    """adds all numbers in list 
    """
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum


def subtract(num_list):
    """subtracts from first number all other numbers"""

    difference = num_list[0]
    i = 1

    while i < len(num_list):
        difference = difference - num_list[i]
        i += 1

    return difference


def multiply(num_list):
    """multiplies all numbers in series
    """
    product = 1
    for num in num_list:
        product = product * num
    return product


def divide(num1, num2):
    """divides all numbers in series
    """
    quotient = num_list[0]
    i = 1

    while i < len(num_list):
        quotient = quotient / num_list[i]
        i += 1

    return quotient

    

def square(num1):
    """squares single input
    """
    return num1 * num1


def cube(num1):
    """cubes single input
    """
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    """raises first number to power of second number 
    """
    return num1 ** num2  # ** = exponent operator


def mod(num_list):
    """successively calulates the modulo 
    """
    modulo = num_list[0]
    i = 1

    while i < len(num_list):
        modulo = modulo % num_list[i]
        i += 1

    return modulo

