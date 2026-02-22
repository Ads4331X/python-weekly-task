
def FizzBuzz(n):
    if( n % 3 == 0 and n % 5 == 0 ): return "FizzBuzz"
    elif( n % 3 == 0 ): return "Fizz"
    elif( n % 5 == 0 ): return "Buzz"
    else: return n

def main():
    n = int(input("Enter a number: "))
    print(FizzBuzz(n))

main()