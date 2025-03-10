""" This program will check to see if the user has entered a valid integer
    in a specific range of numbers"""

# Use constants for the low and high values
LOW = 1
HIGH = 10

# Ask the user to type in a number
num = input("Please enter a integer: ")

# Check to see if the number is an integer
if num.lstrip("-").isnumeric():
    num = int(num)
    if num < LOW:
       print(f"{num} is lower than LOW")
    elif num > HIGH:
        print(f"{num} is greater than HIGH")
else:
      print(f"Your number is {num}")
else:
    print(f"{num} is not an integer") 