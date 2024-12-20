from math import *
a, b = map(int, input("Enter:").split())
h = 2
x = 1
summa = 0
while x <= 12:
    r1 = b + sin(x)
    r2 = (a**3) + (cos(x**3) ** 2)
    summa += (a**2) + ((r1 / r2) ** (1 / 5))

    x += h

print(f"{summa:.2f}")


