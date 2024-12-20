from math import sqrt, log, pi, tan, cos, log2, e, atan, sin
a, b = map(float, input().split())


r1 = a ** (1/5)
r2 = sqrt(sqrt(b * ((a + b) / ((2 * b) + (a * b)))))
r3 = a ** 2 + b ** 2 + 2
result = r1 + r2 * r3
print(f"{result:.2f}")

