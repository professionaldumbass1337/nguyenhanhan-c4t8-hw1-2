import math

loop = True
while loop == True:
    try:
        r = float(input("Please enter the radius of the circle: "))

        if r <= 0 :
           pass
        else:
            pi = math.pi
            area = r*r*pi
            area_round = round(area, 2)

            print("The area of the circle:", area_round)
            
            ask = input("Press E to exit or another key to continue ")
            if ask == "e" or ask == "E":
                loop = False
            else:
                pass
        
    except :
       pass
