"""
Program to create Staff class, store multiple staff records, save to CSV file,
and display them with file handling and exception handling.
"""

import os
file_name = "staff.csv"

class Staff:
    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary

    def __str__(self):
        return (f"  Employee ID    : {self.emp_id}\n"
                f"  Full Name      : {self.full_name}\n"
                f"  Address        : {self.address}\n"
                f"  Phone Number   : {self.phone_number}\n"
                f"  Marital Status : {self.marital_status}\n"
                f"  Dependents     : {self.dependents}\n"
                f"  Salary         : {self.salary}")

    def to_csv_line(self):
        """Returns a CSV-formatted line for this staff member."""
        return f"{self.emp_id},{self.full_name},{self.address},{self.phone_number},{self.marital_status},{self.dependents},{self.salary}\n"


# Validation helpers 

def validate_input(prompt):
    """Validates that a text field is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Error: This field cannot be empty.")


def validate_salary(prompt):
    """Validates that salary is a valid positive number."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("  Error: Salary cannot be empty.")
            continue
        try:
            salary = float(value)
            if salary < 0:
                print("  Error: Salary cannot be negative.")
                continue
            return salary
        except ValueError:
            print("  Error: Salary must be a valid number.")


def validate_dependents(prompt):
    """Validates that dependents is a non-negative whole number."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("  Error: Dependents cannot be empty.")
            continue
        if not value.isdigit():
            print("  Error: Dependents must be a whole number (0 or more).")
            continue
        return int(value)


# Core functions 
def save_to_file(staff_list):
    """Writes all staff records to staff.csv with proper header handling."""
    try:
        file_exists = os.path.exists(file_name)

        with open(file_name, "a") as f:
            # write header only once
            if not file_exists:
                f.write("emp_id,full_name,address,phone_number,marital_status,dependents,salary\n")

            for staff in staff_list:
                f.write(staff.to_csv_line())

    except IOError as e:
        print(f"Error writing file: {e}")

def display_all_records():
    """Reads and displays all records from staff.csv. Uses try/except for file errors."""
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()[1:]  # skip header row

        print("\n" + "=" * 50)
        print("           ALL STAFF RECORDS")
        print("=" * 50)

        for i, line in enumerate(lines, start=1):
            data = line.strip().split(",")
            print(f"\n  Record #{i}")
            print(f"  Employee ID    : {data[0]}")
            print(f"  Full Name      : {data[1]}")
            print(f"  Address        : {data[2]}")
            print(f"  Phone Number   : {data[3]}")
            print(f"  Marital Status : {data[4]}")
            print(f"  Dependents     : {data[5]}")
            print(f"  Salary         : {data[6]}")
            print("  " + "-" * 40)

    except FileNotFoundError:
        print(f"  Error: '{file_name}' not found.")
    except IOError as e:
        print(f"  Error: Could not read file. {e}")


# Main program 

staff_list = []

print("Enter staff details. Type 'done' as Employee ID to stop.\n")

while True:
    print("--- Enter Staff Details ---")
    emp_id_input = input("Enter employee ID (or 'done' to stop): ").strip()

    # User intentionally wants to stop
    if emp_id_input.lower() == "done":
        break

    if not emp_id_input.isdigit() or int(emp_id_input) <= 0:
        print("  Error: Employee ID must be a positive number. Try again.")
        continue

    try:
        full_name  = validate_input("Enter full name       : ")
        address    = validate_input("Enter address         : ")
        phone      = validate_input("Enter phone number    : ")
        marital    = validate_input("Enter marital status  : ")
        dependents = validate_dependents("Enter dependents      : ")
        salary     = validate_salary("Enter salary          : ")

        staff = Staff(int(emp_id_input), full_name, address, phone, marital, dependents, salary)
        staff_list.append(staff)
        save_to_file(staff_list)
        print("\n  Staff member added successfully.\n")

    except Exception as e:
        print(f"  Unexpected error: {e}")

# Display all records after the user is done entering
if staff_list:
    display_all_records()
else:
    print("\n  No staff members were added.")