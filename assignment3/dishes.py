"""
Program to create a Dish class and manage a collection of dishes using Cookbook class.
"""

# Class representing a single Dish
class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return (f"Dish ID: {self.dish_id}\n"
                f"Dish Name: {self.dish_name}\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Instructions: {self.instructions}\n")


# Class representing the Cookbook
class CookBook:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def display_dishes(self):
        if not self.dishes:
            print("No dishes in the cookbook.")
        else:
            for dish in self.dishes:
                print(dish)


# Input validation functions
def validate_dish_id(prompt):
    while True:
        value = input(prompt)
        if value.lower() == 'exit':
            return None
        if not value.strip():
            print("Dish ID cannot be empty.")
            continue
        if not value.isdigit():
            print("Dish ID must be numeric.")
            continue
        return int(value)


def validate_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("Input cannot be empty. Please enter a valid value.")


# Main program
cookbook = CookBook()

while True:
    dish_id = validate_dish_id("Enter dish ID (or 'exit' to stop): ")
    if dish_id is None:
        break

    dish_name = validate_input("Enter dish name: ")
    
    # Ingredients: remove empty entries and extra spaces
    ingredients = [i.strip() for i in validate_input(
        "Enter ingredients (comma-separated): ").split(',') if i.strip()]
    
    instructions = validate_input("Enter instructions: ")

    dish = Dish(dish_id, dish_name, ingredients, instructions)
    cookbook.add_dish(dish)

# Display all dishes in the cookbook
print("\nCookbook:")
cookbook.display_dishes()