"""
Write a program to compute the factorial of a number entered by the user. Ensure the
input is a valid positive integer. If the user enters anything else, display an error
message such as “Invalid input! Please enter a positive integer.”
"""

def factorial(n): # function to calculate factorial of a number
    if n == 0 or n == 1: return 1
    else: return factorial(n - 1) * n

# Taking input for the number and validating it
while True: 
    try:
        num = int(input("Enter a positive integer to compute its factorial: "))
        if num >= 0:
            break
        else:
            print("Invalid input! Please enter a positive integer. Try again.")
    except ValueError:
        print("Invalid input! Please enter a positive integer. Try again.")

# Calculating and displaying the factorial  
result = factorial(num)
print(f"The factorial of {num} is: {result}")
print()