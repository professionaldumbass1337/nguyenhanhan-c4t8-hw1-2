loop = True
while loop == True:
    try:
        month = int(input("Please enter the month: "))
        if month <= 3 and month > 0 :
            print("spring")
        elif month <= 6 and month > 0:
            print("summer")
        elif month <= 9 and month > 0:
            print("autumn")
        elif month <= 12 and month > 0:
            print("winter")
        else : 
            print("Input the month again")
            pass
        
    except ValueError:
        print("Input the month again")
        pass
    
    n = input("Enter E to exit or another key to continue ")
    if n == "e" or n == "E":
        loop = False
    else:
        pass