def SumDiff(num1 , num2 , num3                                                                                       ):    # This function takes two numbers as input and returns their sum and difference.
    sum =num1 + num2 + num3
    diff = num1 - num2 - num3
    return sum, diff
                                                                                                                               

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

sum  , diff = SumDiff(num1 , num2 , num3)

print(f"The sum of {num1} and {num2} and {num3} is {sum}")
print(f"The difference of {num1} and {num2} and {num3} is {diff}") 