"""
Write a program to ask details of 3 movies (title, director, release year, rating). Store them in a
dictionary and display the information in a well-formatted manner.
"""
 
def get_info():
    movie_info = []
    ask_details = ["title", "director", "release year", "rating"]

    for i in range(3):
        movie = {}
        print(f"\nEnter the details of movie {i+1}:")
        for detail in ask_details:
            while True:
                try:
                    if detail == "release year":
                        value = input("Enter the release year: ").strip()
                        if value == "":
                            print("Release year cannot be empty.")
                            continue
                        value = int(value)

                    elif detail == "rating":
                        value = input("Enter the rating: ").strip()
                        if value == "":
                            print("Rating cannot be empty.")
                            continue
                        value = float(value)
                        if value < 0 or value > 10:
                            print("Rating must be between 0 and 10.")
                            continue

                    else:
                        value = input(f"Enter the {detail}: ").strip()
                        if value == "":
                            print(f"{detail.capitalize()} cannot be empty.")
                            continue

                    movie[detail] = value
                    break  

                except ValueError:
                    print("Invalid input. Please try again.")

        movie_info.append(movie)

    return movie_info

info = get_info()

print("\nMovie Details:\n")
for i in range(len(info)):
    print(f"Movie {i+1}:")
    for key, value in info[i].items():
        print(f"{key.capitalize()}: {value}")
    print()









