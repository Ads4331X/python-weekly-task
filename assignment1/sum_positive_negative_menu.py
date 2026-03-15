"""
Write a menu-driven program that repeatedly asks the user for numbers and computes
the separate sums of positive and negative numbers. Continue until the user chooses
to exit the program.
"""

positive_sum = 0
negative_sum = 0

while True:
    print("\nMenu:")
    print("1. Enter a number")
    print("2. Exit")
    choice = input("Choose an option (1 or 2): ")   
    try:
        if choice == '1':
            num = float(input("Enter a number: "))
            if num > 0:
                positive_sum += num
            elif num < 0:
                negative_sum += num
        elif choice == '2':
            print(f"\nSum of positive numbers: {positive_sum}")
            print(f"Sum of negative numbers: {negative_sum}")
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
