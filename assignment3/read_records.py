"""
Program to read records.csv and display contents (skipping header row).
"""

try:
    with open("records.csv", "r") as file:
        next(file)  # skip header row
        for line in file:
            data = line.strip().split(",")
            print("Student Name:", data[0])
            print("Roll No:", data[1])
            print("Program:", data[2])
            print("Year:", data[3])
            print("Group:", data[4])
            print("-" * 30)

except FileNotFoundError:
    print("Error: records.csv file not found.")

except Exception as e:
    print("Unexpected error:", e)