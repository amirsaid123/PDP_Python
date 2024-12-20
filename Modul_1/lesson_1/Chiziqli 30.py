from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
x, y, z = map(float, input().split())

r1 = (2 ** (-x))
r2 = sqrt(x + sqrt(sqrt(abs(y) + 2)))
r3 = (((e ** (x-1) )/ (sin(z + 2))) + 2) ** (1 / 3)
result = r1 * r2 * r3
print(f"{result:.2f}")