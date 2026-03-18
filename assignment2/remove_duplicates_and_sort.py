"""
Write a program to accept a list of numbers from the user and return a new list with all duplicates
removed and the numbers sorted in ascending order.
"""

def remove_duplicates_and_sort(numbers):
    unique_numbers = set(numbers)  # Remove duplicates using a set
    sorted_numbers = sorted(unique_numbers)  # Sort the unique numbers
    return sorted_numbers

while True:
    try:
        user_input = input("Enter a list of numbers separated by commas: ")
        number_list = [int(num.strip()) for num in user_input.split(",")]
        result = remove_duplicates_and_sort(number_list)
        print("Sorted list with duplicates removed:", result)
        break
    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by commas.")
