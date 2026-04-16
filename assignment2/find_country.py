"""
Write a function that accepts two parameters: a list of countries and the country to be searched. The
function should return the index of the country if found. Otherwise, it should return the
message “Not Found in List”.
"""

def find_country(countries , country_to_find):
    if country_to_find in countries:
        return countries.index(country_to_find)
    else:
        return "Not Found in List"
    
countries = []
while True:
    country = input("Enter a country: ")
    countries.append(country)

    if input("Do you want to enter another country? (y/n): ").lower() != "y":
        break

country_to_find = input("Enter the country to search for: ")
result = find_country(countries, country_to_find)
print(f'Index: {result}')
print(f"Countries: {countries}")




















