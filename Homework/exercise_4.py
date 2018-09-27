from random import random
from random import randint
loop = True
while loop == True:
    n = input("Enter any key to start the programme or press E to exit ")
    if n == "E" or n == "e":
        loop = False
    else:
        a = random()
        b = randint(0, 100)
        c = a + b
        print(c)
        if c < 30 :
            print("Rainy")
        elif c >= 30 and c < 60:
            print("Cloudy")
        else:
            print("Sunny")