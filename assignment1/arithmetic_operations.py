"""
Write a program to take two integer inputs from the user and display the results of the
following operations in a clean format: 
I. Addition
II. Multiplication
III. Division
IV. Modulus (remainder)
V. Exponentiation
"""

def addition(a, b): # function to perform addition of two numbers
    return a + b

def multiplication(a, b): # function to perform multiplication of two numbers
    return a * b 

def division(a, b): # function to perform division of two numbers, with error handling for division by zero
    if b != 0:
        return a / b
    else:
        return None  # Handle division by zero

def modulus(a, b): # function to perform modulus operation of two numbers, with error handling for division by zero
    if b != 0:
        return a % b
    else:
        return None  # Handle division by zero

def exponentiation(a, b): # function to perform exponentiation of two numbers
    return a ** b

# Main program
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Storing results of operations in a dictionary for easy access and clean formatting
operations = {
    "Addition": addition(num1, num2),
    "Multiplication": multiplication(num1, num2),
    "Division": division(num1, num2),
    "Modulus": modulus(num1, num2),
    "Exponentiation": exponentiation(num1, num2)
}

# Dictionary to hold symbols for each operation for clean output formatting
symbols = {
    "Addition": "+",
    "Multiplication": "*",
    "Division": "/",
    "Modulus": "%",
    "Exponentiation": "**"
}

# Displaying results in a clean format, with special handling for division by zero cases
print("\n RESULTS ")
for operation, result in operations.items():
    print()
    if operation == "Division" and result is None:
        print(f"{operation}:\n Division by zero is undefined.")
    elif operation == "Modulus" and result is None:
        print(f"{operation}:\n Modulus by zero is undefined.")
    else:
        if operation == "Division":
            print(f"{operation}:\n {num1} {symbols[operation]} {num2} = {result:.2f}")
        else:
            print(f"{operation}:\n {num1} {symbols[operation]} {num2} = {result}")
print()