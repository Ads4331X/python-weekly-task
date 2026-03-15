"""
Write a menu-driven program that repeatedly asks the user for numbers and computes
the separate sums of positive and negative numbers. Continue until the user chooses
to exit the program.
"""

positive_sum = 0
negative_sum = 0

while True: 
    # Displaying the menu options to the user and taking their choice as input
    print("\nMenu:")
    print("1. Enter a number")
    print("2. Exit")
    choice = input("Choose an option (1 or 2): ")   
    # Using a try-except block to handle invalid input and ensure the program continues to run smoothly
    try:
        if choice == '1':
            num = float(input("Enter a number: ")) # taking input from the user and converting it to a float to allow for decimal numbers
            if num > 0: # if the number is positive, add it to the positive_sum
                positive_sum += num
            elif num < 0: # if the number is negative, add it to the negative_sum
                negative_sum += num
        elif choice == '2': # if the user chooses to exit, display the sums of positive and negative numbers and break out of the loop
            print(f"\nSum of positive numbers: {positive_sum}")
            print(f"Sum of negative numbers: {negative_sum}")
            print("Exiting the program. Goodbye!")
            break
        else: # if the user enters an invalid choice, prompt them to choose again
            print("Invalid choice! Please choose 1 or 2.")
    except ValueError: # handling the case where the user input for the number is not a valid float and prompting them to try again
        print("Invalid input! Please enter a valid number.")
