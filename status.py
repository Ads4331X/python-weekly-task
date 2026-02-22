

def Status():   
    credit_earned = int(input("Enter the number of college credit earned: "))
    while credit_earned > 100 or credit_earned < 0:
            print("Please enter a valid credit score")
            credit_earned = int(input("Enter the number of college credit earned: "))    
    if(credit_earned >= 90):
        print("Senior Status")
    elif credit_earned >= 60 :
        print("Junior Status")
    elif credit_earned >= 30 :
        print("Sophomore Status")
    else:
        print("Freshman Status")

Status()


