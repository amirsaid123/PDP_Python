from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
a, x = map(float, input().split())

r1 = x * sin(x / 2 + x / 3 + x / 4)
r2 = log((x**2) - 2) + (3**a)
r3 = cos(x+3) * sin(x+3) + 8
result = r1 + (r2 / r3)
print(f"{result:.2f}")