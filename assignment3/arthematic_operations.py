"""
Program to take numbers from user, perform arithmetic operations,
save results with datetime, and display file content.
"""

from datetime import datetime

file_name = "arithmetic_results.txt"

numbers = []
total_sum = 0
difference = None
product = 1
quotient = None

print("Enter numbers (type any non-number to stop):")

while True:
    try:
        num = input("Enter number: ")

        num = float(num)  # may raise ValueError
        numbers.append(num)

        # Addition
        total_sum += num

        # Subtraction
        if difference is None:
            difference = num
        else:
            difference -= num

        # Multiplication
        product *= num

        # Division
        if quotient is None:
            quotient = num
        else:
            if num != 0:
                quotient /= num
            else:
                print("Warning: Division by zero ignored.")

    except ValueError:
        break

# current datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# write results to file
try:
    with open(file_name, "a") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Date & Time: {current_time}\n")
        file.write(f"Numbers: {numbers}\n")
        file.write(f"Sum: {total_sum}\n")
        file.write(f"Difference: {difference}\n")
        file.write(f"Product: {product}\n")
        file.write(f"Quotient: {quotient}\n")
        file.write("=" * 50 + "\n")

    print("\nResults saved successfully!")

except Exception as e:
    print("File error:", e)

# display file content
try:
    print("\n--- File Content ---\n")
    with open(file_name, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")