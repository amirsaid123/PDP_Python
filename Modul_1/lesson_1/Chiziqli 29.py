from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
a, x, y = map(float, input().split())

r1 = (y**2) + (e**x)
r2 = sqrt((e**x) + (a / ((x**2) + 2)))
r3 = (cos(x)**2) / (sin(x)**2) + (cos(x)**3)
result = sqrt(r1 + r2 + r3)
print(f"{result:.2f}")