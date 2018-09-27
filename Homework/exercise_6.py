loop = True
while loop == True:
    username = input("Please input your username: ")

    if username != "techkids":
        print("You are not superuser")

    elif username == "techkids" :
        password = input("Please input the pass word: ")
        if password == "codethechange":
            print("Welcome, superuser")
        else:
            print("Invalid password")
    
    n = input("Press E to exit or another key to continue ")
    if n == "e" or n == "E":
        loop = False
    else:
        pass
