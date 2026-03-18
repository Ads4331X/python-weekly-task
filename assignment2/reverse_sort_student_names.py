"""
Write a function that accepts a list of student names and returns the names sorted in reverse
alphabetical order.
"""

def reverse_sort_student_names(names):
    return sorted(names, reverse=True)

names = []
while True:

    name = input("Enter student name: ")
    names.append(name)

    if input("Do you want to enter another name? (y/n): ").lower() != "y":
        break

sorted_names = reverse_sort_student_names(names)
print("Student names in reverse alphabetical order:", sorted_names)