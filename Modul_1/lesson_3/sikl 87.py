from math import *
a = int(input("Enter:"))
x = -(pi/2)
h = pi / 10
summa = 0
while x <= pi:
    summa += 2 * ((a**(sin(2*x))) ** (1/3)) + (x**2) * cos(a*x)

    x += h

print(f"{summa:.2f}")