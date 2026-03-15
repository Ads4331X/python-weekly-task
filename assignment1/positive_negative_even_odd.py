"""
Write a program that prompts the user to enter a number and determines whether it
is positive, even, positive odd, negative, or negative odd.
"""

number = int(input("Enter a number: ")) # taking input from the user and converting it to an integer

# Checking if the number is positive, negative, even, or odd and printing the appropriate message
if number > 0 and number % 2 == 0: 
    print(f"{number} is a positive even number.")
elif number > 0 and number % 2 != 0:
    print(f"{number} is a positive odd number.")
elif number < 0 and number % 2 == 0:
    print(f"{number} is a negative even number.")
elif number < 0 and number % 2 != 0:    
    print(f"{number} is a negative odd number.")
else:
    print(f"{number} is zero, which is neither positive nor negative, and is considered even.")

