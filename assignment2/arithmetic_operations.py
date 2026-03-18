def addition(a, b): # function to perform addition of two numbers
    return a + b

def multiplication(a, b): # function to perform multiplication of two numbers
    return a * b 

def division(a, b): # function to perform division of two numbers, with handling for division by zero
    if b != 0:
        return a / b
    else:
        return None

def floor_division(a, b): # function to perform floor division of two numbers, with handling for division by zero
    if b != 0:
        return a // b
    else:
        return None

def exponentiation(a, b): # function to perform exponentiation of two numbers
    return a ** b


# Main program
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Storing results of operations in a dictionary for cleaner output formatting
operations = {

    "Addition": addition(num1, num2),
    "Multiplication": multiplication(num1, num2),
    "Division": division(num1, num2),  # FIXED
    "Floor Division": floor_division(num1, num2),
    "Exponentiation": exponentiation(num1, num2)
}

symbols = {
    "Addition": "+",
    "Multiplication": "*",
    "Division": "/",  
    "Floor Division": "//",
    "Exponentiation": "**"
}

# Displaying results in a clean format, with special handling for division by zero cases
print("\nRESULTS")
for operation, result in operations.items():
    print()
    if result is None:
        print(f"{operation}:\n Undefined (division by zero).")
    else:
        if operation == "Division":
            print(f"{operation}:\n {num1} {symbols[operation]} {num2} = {result:.2f}")
        else:
            print(f"{operation}:\n {num1} {symbols[operation]} {num2} = {result}")