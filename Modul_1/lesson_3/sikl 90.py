from math import *
a, b, c = map(int, input("Enter:").split())
h = pi / 10
x = -pi
summa = 0
while x <= pi:
    r1 = log(a**(sin(x) * 2)) + e**(2*x)
    r2 = atan(x) + b
    summa += r1 / r2 + c

    x += h

print(f"{summa:.2f}")


