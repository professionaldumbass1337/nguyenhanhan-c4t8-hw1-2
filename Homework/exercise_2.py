loop = True
while loop == True:
    month = int(input("Please enter the month: "))
    if month <= 3 and month >= 0 :
        print("spring")
    elif month <= 6:
        print("summer")
    elif month <= 9:
        print("autumn")
    elif month <= 12:
        print("winter")
    else : 
        pass