"""
Program to take at least 12 numbers from user, sort them and perform slicing operations.
"""

# Take input (at least 12 numbers)
numbers = list(map(int, input("Enter at least 12 numbers separated by space: ").split()))

# Check if user entered at least 12 numbers
if len(numbers) < 12:
    print("Please enter at least 12 numbers.")
else:
    # Sort the list
    numbers.sort()

    print("Sorted List:", numbers)

    # Slicing operations
    print("Elements from index 3 to 6:", numbers[3:7])   # 3 to 6
    print("Elements from index 6 to 9:", numbers[6:10])  # 6 to 9
    print("Elements from index 4 to 10:", numbers[4:11]) # 4 to 10