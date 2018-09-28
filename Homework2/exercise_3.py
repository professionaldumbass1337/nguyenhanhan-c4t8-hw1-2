from random import randint

loop = True
while loop == True:
    n = input("Press any key to generate a random integer in range [0,100] or press E to exit ")
    if n == "e" or n == "E":
        loop = False
    else:
        a = randint(0, 100)
        print(a)