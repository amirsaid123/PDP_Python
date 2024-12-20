from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
x1, x2, c, d = map(float,  input().split())

r1 = (sin(abs((c * (x2 ** 3)) + (d * (x1 ** 3)) - (c * d)))) ** 2
r2 = sqrt((c + (x1**2)) + (d * (x2 ** 2)) + 7)
r3 = tan(x1 * (x2 ** 2) + (d ** 3))
result = abs(r1 / r2) + r3
print(f"{result:.2f}")