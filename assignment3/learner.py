"""
Program to create a Learner class, take user input, and display details.
"""

class Learner:
    def __init__(self, full_name, roll_no, program, enrollment_year, group, address):
        self.roll_no = roll_no
        self.full_name = full_name       
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def __str__(self):
        return (f"\nName:             {self.full_name}"
                f"\nRoll No:          {self.roll_no}"
                f"\nProgram:          {self.program}"
                f"\nEnrollment Year:  {self.enrollment_year}"
                f"\nGroup:            {self.group}"
                f"\nAddress:          {self.address}")


# Input validation functions
def validate_roll_no(prompt):
    """Validates that roll number is not empty and is numeric."""
    while True:
        value = input(prompt)
        if not value.strip():
            print("Roll number cannot be empty.")
            continue
        if not value.isdigit():
            print("Roll number must be numeric.")
            continue
        return int(value)


def validate_input(prompt):
    """Validates that input is not empty."""
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("Input cannot be empty. Please enter a valid value.")


# Function to get learner details from the user
def get_learner_info():
    """Takes all learner details from the user and returns a Learner object."""
    name = validate_input("Enter learner's full name: ")
    roll_no = validate_roll_no("Enter learner's roll number: ")
    program = validate_input("Enter learner's program: ")
    enrollment_year = validate_input("Enter learner's enrollment year: ")
    group = validate_input("Enter learner's group: ")
    address = validate_input("Enter learner's address: ")

    return Learner(name, roll_no, program, enrollment_year, group, address)


# Create a Learner object and display details
learner = get_learner_info()
print("\n--- Learner Details ---")
print(learner)