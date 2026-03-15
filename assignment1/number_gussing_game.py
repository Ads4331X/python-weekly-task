"""
Write a number guessing game in Python with the following rules:
 The computer generates a random number between 1 and 50.
 The user must guess the number.
 After each guess, the program tells the user whether the guess is too high, too low,
or correct.
 The user gets a maximum of 7 attempts.

 If the user does not guess correctly within the attempts, display “Better luck next
time!” and end the game."""

import random

max_attempts = 7
random_number = random.randint(1, 50) # generating a random number between 1 and 50 using the random module
current_attempt = 0 # variable to keep track of the current attempt number
print("Welcome to the Number Guessing Game!\nYou have 7 attempts to guess the number between 1 and 50. Good luck!\n")
print(f"(For testing purposes, the random number is: {random_number})\n")  
while current_attempt < max_attempts:
    try:
        user_guess = int(input(f"Attempt no {current_attempt + 1}: Guess the number between 1 and 50: ")) # taking input from the user and converting it to an integer
        if(user_guess < 1 or user_guess > 50): # validating the user input to ensure it's between 1 and 50
            print("Invalid input! Please enter a number between 1 and 50. Try again.")
            continue
        # checking if the user's guess is too low, too high, or correct and printing the appropriate message
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        # if the guess is correct, congratulate the user and break out of the loop
        else:
            print(f"Congratulations! You've guessed the number {random_number} correctly in {current_attempt + 1} attempts!")
            break
        current_attempt += 1 # incrementing the attempt counter after each valid guess
    except ValueError: # handling the case where the user input is not a valid integer and prompting them to try again
        print("Invalid input! Please enter a valid integer. Try again.")

 # if the user has used all attempts without guessing correctly, display the "Better luck next time!" message along with the correct number
if current_attempt == max_attempts:
    print(f"Better luck next time! The correct number was {random_number}.")