import math
r = float(input("Please enter the radius of the circle: "))

pi = math.pi
area = r*r*pi
area_round = round(area, 2)

print("The area of the circle:", area_round)