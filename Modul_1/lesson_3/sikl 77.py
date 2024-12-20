from math import *
a, b, c, d = map(int, input("Enter:").split())
h = 2
summa = 0
x = c

while x <= d:
    r1 = sin(a*x) + b**(2*c)
    r2 = (b**2) + (cos(x)**2)
    r3 = sin(x**2) / (a*b)
    result = ((r1 / r2) ** (1/3)) - r3
    summa += result

    x+=h

print(f"{summa:.2f}")
