"""
Write a program to find all numbers between 1000 and 2500 (inclusive) that are
divisible by 9 but not by 6. Extend the program so that the range limits (1000 and 2500)
can also be entered by the user.
"""

# Displaying numbers divisible by 9 but not by 6 between 1000 and 2500
print("Number divisible by 9 but not by 6 between 1000 and 2500 (inclusive):")
for num in range(1000, 2501):
    if num % 9 == 0 and num % 6 != 0:
        print(num)
print()

# Taking input for range limits
while True:
    try:
        start_range = int(input("Enter the starting number of the range: "))
        end_range = int(input("Enter the ending number of the range: "))
        if start_range <= end_range:
            break
        else:
            print("Invalid input! Starting number must be less than or equal to ending number. Try again.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Displaying numbers divisible by 9 but not by 6 in the user-defined range
print(f"Number divisible by 9 but not by 6 between {start_range} and {end_range} (inclusive):")
for num in range(start_range, end_range + 1):
    if num % 9 == 0 and num % 6 != 0:
        print(num)  
