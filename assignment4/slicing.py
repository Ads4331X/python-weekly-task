"""
Program to take at least 12 numbers from user, sort them and perform slicing operations.
"""

# Take input (at least 12 numbers)
while True:
    numbers = list(map(int, input("Enter at least 12 numbers separated by space: ").split()))
    if len(numbers) >= 12: # check if user entered atleast 12 numbers
        break
    print("  Error: Please enter at least 12 numbers. Try again.")

numbers.sort() # sort the list 
print("Sorted List:", numbers)
# slicing operations
print("Elements from index 3 to 6:", numbers[3:7]) # 3 to 6
print("Elements from index 6 to 9:", numbers[6:10]) # 6 to 9
print("Elements from index 4 to 10:", numbers[4:11]) # 4 to 10