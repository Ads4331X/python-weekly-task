"""
Write a program to take two integer inputs from the user and display the results of the
following operations in a clean format: 
I. Addition
II. Multiplication
III. Division
IV. Modulus (remainder)
V. Exponentiation
"""


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

add = num1 + num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else None
mod = num1 % num2 if num2 != 0 else None
exp = num1 ** num2

# Displaying results in a clean format, with special handling for division by zero cases
print("\n RESULTS ")

print(f"Addition: {num1} + {num2} = {add}")
print(f"Multiplication: {num1} * {num2} = {mul}")
if div is None:
    print("Division: Division by zero is undefined.")
else:
    print(f"Division: {num1} / {num2} = {div:.2f}")
if mod is None:
    print("Modulus: Modulus by zero is undefined.")
else:
    print(f"Modulus: {num1} % {num2} = {mod}")
print(f"Exponentiation: {num1} ** {num2} = {exp}")
print()