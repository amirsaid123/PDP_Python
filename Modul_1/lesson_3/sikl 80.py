from math import *
a = int(input("Enter:"))
h = 0.5
x = 0
summa = 0
while x <= 10:
    summa += a * cos(x) - sin(x**2)

    x += h

print(f"{summa:.2f}")


