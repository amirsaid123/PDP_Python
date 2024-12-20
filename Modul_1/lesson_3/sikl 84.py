from math import *
a, b, c= map(int, input("Enter:").split())
h = 0.25
x = -1
summa = 0
while x <= 1:
    r1 = sin(a*x) + (b**c)
    r2 = (b**2) + (cos(x) ** 2)
    r3 = (sin(x**2)) / (a*b)
    summa += ((r1 / r2) ** (1 / 3)) - r3

    x += h

print(f"{summa:.2f}")


