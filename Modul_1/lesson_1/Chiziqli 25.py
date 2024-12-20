from math import sqrt, log, pi, tan, cos, log2, e, atan, sin, log10
a, x = map(float, input().split())

r1 = sqrt(x - 1) + sqrt(x + 2) + log10(sqrt(a * (x ** 2)) + 2)
r2 = sqrt(sqrt(x + 2) + sqrt(x + 24) + (x**5))
result = r1 / r2
print(f"{result:.2f}")