from math import *
a, b, c= map(int, input("Enter:").split())
h = 0.5
x = 5
summa = 0
while x <= 10:
    summa +=((a**2) + (b*x) + (x**c)) / ((a**2) + (b**2) + (x**2))

    x += h

print(f"{summa:.2f}")


