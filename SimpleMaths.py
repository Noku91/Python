"""This program will ask the user for their name and favourite numbers
and then perform some simple maths on the numbers"""

# Ask the user for their name and their favourite numbers
name = input("What is your name? ")
number1 = int(input("what is your favourite number? "))
number2 = int(input("What is your second favourite number? "))

# Perform some simple maths on the numbers
add = number1 + number2
multiply = number1 * number2

# Greet the user and print the results
print(f"Hi {name}, here are some fun calculations with your favourite numbers: ")
print(f"{number1} + {number2} = {add}")
print(f"{number1} * {number2} = {multiply}")