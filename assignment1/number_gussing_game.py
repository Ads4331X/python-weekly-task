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
random_number = random.randint(1, 50)
current_attempt = 0
print("Welcome to the Number Guessing Game!\nYou have 7 attempts to guess the number between 1 and 50. Good luck!\n")
print(f"(For testing purposes, the random number is: {random_number})\n")  # You can comment this line out in the actual game
while current_attempt < max_attempts:
    try:
        user_guess = int(input(f"Attempt no {current_attempt + 1}: Guess the number between 1 and 50: "))
        if(user_guess < 1 or user_guess > 50):
            print("Invalid input! Please enter a number between 1 and 50. Try again.")
            continue
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} correctly in {current_attempt + 1} attempts!")
            break
        current_attempt += 1
    except ValueError:
        print("Invalid input! Please enter a valid integer. Try again.")

if current_attempt == max_attempts:
    print(f"Better luck next time! The correct number was {random_number}.")