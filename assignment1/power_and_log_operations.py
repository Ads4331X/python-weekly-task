"""
Write a program to take a single number as input and display: 
I. Cube of the number
II. Cube root of the number
III. Natural logarithm of the number
IV. Base-2 logarithm of the number
V. The number raised to the power of 6
"""

e = 2.718281828459045   # Euler's number
ln2 = 0.6931471805599453  # Natural log of 2

number = float(input("Enter a number: "))

# Calculations
cube = number ** 3
cube_root = number ** (1/3)

# Approximation of ln(x)
natural_log = e * (number ** (1/e) - 1)

# log2(x) = ln(x) / ln(2)
base2_log = natural_log / ln2

power_of_6 = number ** 6

print(f"\nNumber entered: {number}")

print("\nResults:")
print(f"Cube of {number}                       : {cube:.4f}")
print(f"Cube root of {number}                  : {cube_root:.4f}")
print(f"Natural logarithm of {number}          : {natural_log:.4f}")
print(f"Base-2 logarithm of {number}           : {base2_log:.4f}")
print(f"{number} raised to the power of 6      : {power_of_6:.4f}")
print()