from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
a, b, c, d, x = map(float, input().split())

r1 = (a * (x**2)) + (b * x) + c
r2 = x * (a**3) + (a**2) + (a ** (b-c))
r3 = cos(abs(((a * x) + b) / ((c * x) + d + (2 ** c))))
result = (r1 / r2) + r3
print(f"{result:.2f}")