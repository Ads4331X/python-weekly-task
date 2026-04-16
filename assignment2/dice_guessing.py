"""
10. Create a program to design a dice guessing game with the following specifications: 
I. The dice has values from 1 to 6.
II. The program should generate a random value for the dice roll.
III. The player should guess the dice value.
IV. If the guess is correct, show a smiling face.
V. If the guess is off by 1 (e.g., dice = 5, guess = 4), show a neutral face.
"""

import random

def dice_guessing_game():
    attempts = 0
    dice_value = random.randint(1 , 6) # Generate a random value for the dice roll from 1 to 6
    print(f'For testing purpose dice number: {dice_value}')



    while True:
        try:
            guess = int(input("Guess the dice value (1-6): "))
            if guess < 1 or guess > 6:
                print("Please enter a number between 1 and 6.")
                continue
            if guess == dice_value:
                print("Correct! You guessed the dice value.")
                print(f"It took you {attempts + 1} attempts to guess the correct value.")
                break
            elif abs(guess - dice_value) == 1:
                print("Close! Your guess is off by 1.")
                attempts += 1
            else:
                print("Incorrect! Better luck next time.")
                attempts += 1

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

dice_guessing_game()

