name = "ads"
password = "12345"


while True:
	user_Input = input("Enter the username: ")
	user_Password = input("Enter the password: ")
	if user_Input.lower() != name.lower() or user_Password.lower() != password.lower():
		print("Please Enter Corret Username and Passowrd")
	else: break
		



print("Logined Successfully")
