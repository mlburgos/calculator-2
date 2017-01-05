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

def calculator():
    while True:
        request = raw_input("> ")

        if request == "q":
            return

        components = request.rstrip().split(" ")
        math_func = components[0]
        num_list = components[1:]


        if (math_func == 'square' or math_func == 'cube') and len(num_list) > 1:
            print "I can only take one argument for that operation"
            continue

        try:
            i = 0
            while i < len(num_list):
                num_list[i] = int(num_list[i])
                i += 1

        except ValueError:
            print "numbers only, please! try again."
            continue

        if math_func == "+":
            print my_reduce(add, num_list)
        elif math_func == "-":
            print my_reduce(subtract, num_list)
        elif math_func == "*":
            print my_reduce(multiply, num_list)
        elif math_func == "/":
            print my_reduce(divide, num_list)
        elif math_func == "square":
            print square(num_list[0])
        elif math_func == "cube":
            print cube(num_list[0])
        elif math_func == "pow":
            print my_reduce(power, num_list)
        elif math_func == "mod":
            print my_reduce(mod, num_list)
        else:
            print "I don't recognize your request :("
            continue

calculator()     
