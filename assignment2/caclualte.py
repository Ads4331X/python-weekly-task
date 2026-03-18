"""
Write a program to create a function that accepts two integers and displays their sum, difference,
product, quotient values."""

def calculate(a, b): # function to perform arithmetic operations on two numbers

    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None  # Handle division by zero case

    return sum_result, difference_result, product_result, quotient_result

# Main program
num1 = int(input("Enter the first integer: "))      
num2 = int(input("Enter the second integer: "))

sum_, difference, product, quotient = calculate(num1, num2)  # calling the calculate function with user inputs

# Displaying the results
print(f"Sum: {sum_}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient if quotient is not None else 'Division by zero is undefined.'}")
