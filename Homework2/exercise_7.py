loop = True

while loop == True :
    try :
        a = float(input("Input the coefficient a of the equation ax^2+bx+c: "))
        b = float(input("Input the coefficient b of the equation ax^2+bx+c: "))
        c = float(input("Input the coefficient c of the equation ax^2+bx+c: "))

        if a == 0:
            if b == 0 :
                if c == 0 :
                    print("The quation has many solutions")
                if c != 0 :
                    print("The equation has no solution")
            else :
                x = - c / b
                print(x)
        
        if a != 0:
            delta = b*b - 4*a*c
            if delta < 0:
                print("The equation has no solution")
            if delta == 0:
                x = - b / (2*a)
                print("The equation has one solution",x)
            if delta > 0:
                x1 = (-b + delta**(1/2))/(2*a)
                x2 = (-b - delta**(1/2))/(2*a)
                print(x1)
                print(x2)
    except ValueError:
        print("Please start the program again ")
        pass

    n = input("Press E to exit or another key to continue ")
    if n == "E" or n == "e":
        loop = False
    else:
        pass