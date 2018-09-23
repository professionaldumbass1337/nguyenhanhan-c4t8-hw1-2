from random import random
from random import randint
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