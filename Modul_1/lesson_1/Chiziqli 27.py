from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
x = float(input("Enter a number: "))

r1 = 2 * (tan(x + 2))
r2 = cos(x + (2 ** x))
r3 = 1 + (cos(x + 2) ** 2)
r4 = (sin(x**2)) / ((x**2) + 3)
result = sqrt((r1 - r2 )/ r3) + r4
print(f"{result:.2f}")