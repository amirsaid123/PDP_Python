from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
a, x, y = map(float, input().split())

r1 = e ** (x*y)
r2 = x * sin(a * x)
r3 = ((x**2) + 2) / (abs(x) + 5)
r4 = sqrt(log((x**2) + 2) + 5)
result = sqrt(r1 - r2 - r3) + r4
print(f"{result:.2f}")