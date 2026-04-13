"""
Append student details to records.csv with validation and error handling.
"""

try:
    with open("records.csv", "a") as file:

        student_name = input("Enter student name: ").strip()
        while not student_name:
            print("Field cannot be empty")
            student_name = input("Enter student name: ").strip()

        roll_no = input("Enter roll number: ").strip()
        while not roll_no:
            print("Field cannot be empty")
            roll_no = input("Enter roll number: ").strip()

        program = input("Enter program: ").strip()
        while not program:
            print("Field cannot be empty")
            program = input("Enter program: ").strip()

        year = input("Enter year: ").strip()
        while not year:
            print("Field cannot be empty")
            year = input("Enter year: ").strip()

        group = input("Enter group: ").strip()
        while not group:
            print("Field cannot be empty")
            group = input("Enter group: ").strip()

        file.write(f"{student_name},{roll_no},{program},{year},{group}\n")
        print("Record added successfully!")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)