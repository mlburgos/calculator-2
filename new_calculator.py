"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# # while True:
#     read input
#     tokenize input
#     if the first token is 'q'
#         quit
#     else
#         decide which math function to call based on first token
def my_reduce(func, num_list):
    """replicating reduce
    """
    x = num_list[0]
    i = 1
    
    while i < len(num_list):
        x = func(x, num_list[i])
        i += 1
    return x

def interactive_calc():
    """Receives user interactive requests from terminal.
    """
    decimal = raw_input(" how many decimals would you like to see? \n")

    while True:
        request = raw_input("> ")

        if request == "q":
            return
        
        print calculator(request, decimal)


def file_calculator(file_name):
    """reads file of calculator requests 
    """
    decimal = "2"   

    calc_file = open(file_name)

    results_file = open("{}_results.txt".format(file_name.rstrip(".txt")), "w")

    for line in calc_file:
        output_line = line.rstrip() + " == " + calculator(line, decimal) + "\n"
        results_file.write(output_line)


def calculator(request, decimal_input):
    """Parses string request and calls arithemtic functions.
    """

    components = request.rstrip().split(" ")
    math_func = components[0]
    num_list = components[1:]


    if (math_func == 'square' or math_func == 'cube') and len(num_list) > 1:
        print "I can only take one argument for that operation"
        return "InputError, stupid!"

    try:
        i = 0
        while i < len(num_list):
            num_list[i] = float(num_list[i])
            i += 1

    except ValueError:
        print "numbers only, please! try again."
        return "ValueError, stupid!"

    if math_func == "+":
        result = my_reduce(add, num_list)
    elif math_func == "-":
        result = my_reduce(subtract, num_list)
    elif math_func == "*":
        result = my_reduce(multiply, num_list)
    elif math_func == "/":
        result = my_reduce(divide, num_list)
    elif math_func == "square":
        result = square(num_list[0])
    elif math_func == "cube":
        result = cube(num_list[0])
    elif math_func == "pow":
        result = my_reduce(power, num_list)
    elif math_func == "mod":
        result = my_reduce(mod, num_list)
    else:
        print "I don't recognize your request :("
        return "RequestError, stupid!"

    output = "%." + decimal_input + "f" 

    return output % result 


file_calculator("calc_requests.txt")
# interactive_calc()