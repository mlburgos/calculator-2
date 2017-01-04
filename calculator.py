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

def calculator():
    while True:
        request = raw_input("> ")
        components = request.split(" ")
        math_func = components[0]

        if len(components) == 2:
            components.append(0)

        try:
            num1 = int(components[1])
            num2 = int(components[2])
        except ValueError:
            print "numbers only, please! try again."
            continue


        if math_func == "q":
            return
        elif math_func == "+":
            print add(num1, num2)
        elif math_func == "-":
            print subtract(num1, num2)
        elif math_func == "*":
            print multiply(num1, num2)
        elif math_func == "/":
            print divide(num1, num2)
        elif math_func == "square":
            print square(num1)
        elif math_func == "cube":
            print cube(num1)
        elif math_func == "pow":
            print power(num1, num2)
        elif math_func == "mod":
            print mod(num1, num2)
        else:
            print "I don't recognize your request :("
            continue

calculator()     
