"""
Write a program to input the marks of 6 subjects. Calculate total, average, percentage,
and grade according to the rules below: 
o Distinction: 85% or above
o First Division: 70% and above
o Second Division: 55% and above
o Third Division: 45% and above
o Fail: Below 45%
"""

# Taking input for marks of 6 subjects and storing them in a list
marks = []
for i in range(1, 7):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i}: "))
            if 0 <= mark <= 100:   # check if mark is valid
                marks.append(mark)
                break
            else:
                print("Invalid input! Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Calculating total, average, and percentage
total_marks = sum(marks)
average_marks = total_marks / len(marks)
percentage = (total_marks / (len(marks) * 100)) * 100

# Determining grade based on percentage

if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

# Displaying results
print(f"\nTotal Marks: {total_marks:.2f}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")