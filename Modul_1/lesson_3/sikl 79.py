from math import *
a = int(input("Enter:"))
h = pi / 19
x = -(pi / 2)
summa = 0
while x <= pi:
    summa += ((a ** a) * (1 / 3)) + ((x**2) * cos(a * x))

    x += h

print(f"{summa:.2f}")


