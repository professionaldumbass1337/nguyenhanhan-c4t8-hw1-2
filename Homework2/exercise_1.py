loop = True

while loop == True:
    try:
        yob = int(input("Your year of birth? "))
        age = 2018 - yob
        if age > 14 :
            print("Please watch this video")
        else :
            print("You are not old enough to watch this video")
        n = input("Enter E to exit or another key to continue ")
        if n == "e" or n == "E":
            loop = False
        else:
            pass
    except ValueError:
        pass