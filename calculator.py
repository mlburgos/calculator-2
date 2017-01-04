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


while True:
    request = raw_input("> ")
    components = request.split(" ")
    math_func = components[0]
    num1 = components[1]
    num2 = components[2]



    if math_func == "q":
        return
    elif math_func == "+":
        return arithmetic.add(num1, num2)
    elif math_func == "-":
        return arithmetic.subtract(num1, num2)
    elif math_func == "*":
        return arithmetic.multiply(num1, num2)
    elif math_func == "/":
        return arithmetic.divide(num1, num2)
    elif math_func == "square":
        return arithmetic.square(num1)
    elif math_func == "cube":
        return arithmetic.cube(num1)
    elif math_func == "pow":
        return arithmetic.power(num1, num2)
    elif math_func == "mod":
        return arithmetic.mod(num1, num2)
    else:
        print "I don't recognize your request :("
        continue

        


