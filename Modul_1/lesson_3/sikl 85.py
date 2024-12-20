from math import *
a, b, c= map(int, input("Enter:").split())
h = 5
x = 1
summa = 0
while x <= 20:
    summa += (a * (x**2) + (b*x) + c) / ((a**2) + (b**2) + (x**2))

    x += h

print(f"{summa:.2f}")


