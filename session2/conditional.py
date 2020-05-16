import math
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
delta = (b**2 - 4*a*c)
if (delta > 0):
    print("x1 = ",float(-b+math.sqrt(delta)) / (2*a))
    print("x2 = ",float(-b-math.sqrt(delta)) / (2*a))
elif (delta == 0):
    print("x = ", float(-b)/(2*a))
else:
    print("vo nghiem")
    