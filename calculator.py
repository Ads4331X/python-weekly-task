
def main():
	a =int(input("Enter a number: "))
	o = input("Enter a operator: ")
	operator =o.strip()
	b =int(input("Enter another number: "))
	if(operator == "+"):print(f"The sum of {a} and {b} is { add(a,b)}")
	elif(operator == "-"): print(f"The diffrence of {a} and {b} is {subtract(a,b)}")
	elif(operator == "*"): print(f"The product of {a} and {b} is {multiply(a,b)}")
	elif(operator == "/"): print(f"The division of {a} and {b} is {divide(a,b)}")
	elif(operator == "^"): print(f"The power of {a} to {b} is {power(a,b)}")
	elif(operator =="%"): print(f"THe remainder of {a} to {b} is {remainder(a,b)}")
	else: print("Enter a valid operator")

def add(a , b): return a + b
def subtract(a,b): return a-b
def multiply(a,b): return a *b
def divide(a,b): 
	if(b == 0):
		return("The denometer can not be 0")
	else: return a/b
def power(a,b): return a**b
def remainder(a,b): return a % b

main()

