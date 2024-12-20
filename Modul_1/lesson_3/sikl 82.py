from math import *
a, b, c= map(int, input("Enter:").split())
h = 3
x = 1
summa = 0
while x <= 10:
    summa += ((a * (x**2)) / b) + (x / c)

    x += h

print(f"{summa:.2f}")


