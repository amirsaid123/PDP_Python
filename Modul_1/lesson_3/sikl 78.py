from math import *
a, b, c = map(int, input("Enter:").split())
h = 2
summa = 0
x = a

while x <= b:
    r1 = (a ** b) + (b ** x) + (c ** a)
    r2 = 2 * (x**2) + 3 * (a**x)
    result = r1 / r2
    summa += result

    x+=h

print(f"{summa:.2f}")
