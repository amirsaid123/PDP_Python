from math import *
a, b, c= map(int, input("Enter:").split())
h = 0.25
x = c
summa = 0
while x <= b:
    summa += (a**2) * cos(x) + (sin(x) / 2) + b * (x**2)

    x += h

print(f"{summa:.2f}")


