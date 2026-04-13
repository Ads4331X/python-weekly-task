"""
Program to copy content from one file to another using exception handling.
"""

import os

# Get input and output file names from the user
input_file = input("Enter the input file name: ").strip()
output_file = input("Enter the output file name: ").strip()

try:
    # Check if output file already exists before doing anything
    if os.path.exists(output_file):
        raise FileExistsError(f"Output file '{output_file}' already exists.")

    # Try to open and read the input file
    with open(input_file, "r") as infile:
        content = infile.read()

    # Write content to the output file
    with open(output_file, "w") as outfile:
        outfile.write(content)

    print(f"File copied successfully from '{input_file}' to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: Input file '{input_file}' does not exist.")

except FileExistsError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")