"""
Write a program to display all prime numbers within a user-defined range. Additionally,
print the count of prime numbers in that range along with their sum.
"""

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to get prime numbers in a given range
def primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Taking input for the range
while True:
    try:
        start_range = int(input("Enter the starting number of the range: "))
        end_range = int(input("Enter the ending number of the range: "))
        if start_range <= end_range:
            break
        else:
            print("Invalid input! Starting number must be less than or equal to ending number. Try again.")
    except ValueError:
        print("Invalid input! Please enter an integer.")


# Displaying results
primes = primes_in_range(start_range, end_range)
print(f"Prime numbers in the range {start_range} to {end_range}: {primes}")
print(f"Count of prime numbers: {len(primes)}")
print(f"Sum of prime numbers: {sum(primes)}")