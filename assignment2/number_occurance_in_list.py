"""
Write a function that takes a list of numbers as input and returns a dictionary showing how many
times each number occurs in the list. Test this function with at least three different lists.
"""

def count_occurance(num_list): # function to count the occurances of each number in the list
    occurances = {}
    for num in num_list:
        if num in occurances:
            occurances[num] += 1
        else:
            occurances[num] = 1
    return occurances

# Test cases
test_list1 = [1, 2, 2, 3, 4, 4, 4, 5]
test_list2 = [10, 20, 20, 30, 40, 40, 40, 50]
test_list3 = [5, 5, 5, 5, 5]    
test_list4 = [1, 2, 3, 4, 5]  # a test case with unique numbers
counts1 = count_occurance(test_list1)
counts2 = count_occurance(test_list2)
counts3 = count_occurance(test_list3)   
counts4 = count_occurance(test_list4)


print("Test List 1:", test_list1)
print("Occurrences:", counts1)
print()

print("Test List 2:", test_list2)
print("Occurrences:", counts2)
print()

print("Test List 3:", test_list3)
print("Occurrences:", counts3)
print()

print("Test List 4:", test_list4)
print("Occurrences:", counts4)
print()

while True: # validating input to ensure it's a list of integers
    try:
        user_input = input("Enter a list of numbers separated by commas (e.g., 1,2,3): ")
        user_list = [int(x.strip()) for x in user_input.split(",")]
        break
    except ValueError:
        print("Invalid input! Please enter a valid list of integers separated by commas.")

counts_user = count_occurance(user_list)
print("User List:", user_list)
print("Occurrences:", counts_user)