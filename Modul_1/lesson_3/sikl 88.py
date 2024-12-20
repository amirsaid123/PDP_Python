from math import *
a, b, c, d = map(int, input("Enter:").split())
h = 1.5
x = d
summa = 0
while x <= c:
    r1 = (a*x) + b
    r2 = (b**2) + (cos(x) ** 2)
    r3 = sin(x) / (a*b)
    summa += ((r1 / r2) ** (1/5)) - r3

    x += h

print(f"{summa:.2f}")


