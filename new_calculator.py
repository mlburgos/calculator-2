"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from new_arithmetic import *

# # while True:
#     read input
#     tokenize input
#     if the first token is 'q'
#         quit
#     else
#         decide which math function to call based on first token

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
        elif math_func == 'pow' and len(num_list) > 2:
            print "I can only take two arguments for that operation"
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
            print add(num_list)
        elif math_func == "-":
            print subtract(num_list)
        elif math_func == "*":
            print multiply(num_list)
        elif math_func == "/":
            print divide(num_list)
        elif math_func == "square":
            print square(num_list[0])
        elif math_func == "cube":
            print cube(num_list[0])
        elif math_func == "pow":
            print power(num_list[0], num_list[1])
        elif math_func == "mod":
            print mod(num_list)
        else:
            print "I don't recognize your request :("
            continue

calculator()     
