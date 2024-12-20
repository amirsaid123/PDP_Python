from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
x, y = map(float, input().split())

r1 = (x**2) + 1
r2 = (x**2) + (x * y + (y**2)) / ((y**2) + ((y + x * y) / (abs(x * y) + 5)))
r3 = 1
r4 = 1 + cos(x) + (1 / sin(x))
result = (r1 / r2 ) + (r3 / r4)
print(f"{result:.2f}")

