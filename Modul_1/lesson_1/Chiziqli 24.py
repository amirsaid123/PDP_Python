from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
a, b, c, x = map(float, input().split())

r1 = 0.75
r2 = 8.2 * (x**2) + (sqrt(abs((x**3) + 3 * x) + cos(x - 2)))
r3 = (a / 4) + (b / 3) + (c / 2) + 1
result = r1 + (r2 / r3)
print(f"{result:.2f}")