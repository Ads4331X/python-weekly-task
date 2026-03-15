"""
Write a program to take a single number as input and display: 
I. Cube of the number
II. Cube root of the number
III. Natural logarithm of the number
IV. Base-2 logarithm of the number
V. The number raised to the power of 6
"""

import math # importing the math module to perform logarithmic operations

number = float(input("Enter a number: ")) # taking input from the user and converting it to a float to allow for decimal numbers

# Performing the required operations and storing the results in variables
cube = number ** 3
cube_root = number ** (1/3)
natural_log = math.log(number)
base2_log = math.log2(number)
power_of_6 = number ** 6    

print(f"\nNumber entered: {number}")
# Displaying results 
print("\nResults:") 
print(f"Cube of {number}                       : {cube:.4f}")
print(f"Cube root of {number}                  : {cube_root:.4f}")
print(f"Natural logarithm of {number}          : {natural_log:.4f}")  
print(f"Base-2 logarithm of {number}           : {base2_log:.4f}")
print(f"{number} raised to the power of 6      : {power_of_6:.4f}")
print()