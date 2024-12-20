from math import *
a, b, c = map(int, input("Enter:").split())
h = 3
summa = 0
x = a

while x <= c:
    r1 = a * x + b
    r2 = (b**2) + (cos(x) ** 2)
    r3 = sin(x**2) / (a*b)
    result = ((r1 / r2) ** (1/3)) - r3
    summa += result

    x+=h

print(f"{summa:.2f}")
