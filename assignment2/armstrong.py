"""
Write a program to create a function that accepts one string as input and checks whether it is
Armstrong or not. Display the output neatly.
"""

def is_armstrong(str_num): # function to check if a number is an Armstrong number
    res = int(str_num)
    sum = 0
    power = len(str_num)  # The power is determined by the number of digits in the number
    for x in str_num:
        sum += int(x) ** power  # Summing the digits raised to the power

    return res == sum  # An Armstrong number is one where the sum of its own digits each raised to the power of the number of digits equals the number itself


while True: # validating input to ensure it's an integer
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if(is_armstrong(str(num))):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


print()

