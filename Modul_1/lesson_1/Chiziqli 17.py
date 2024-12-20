x, y = map(float, input().split())
from math import sqrt, log, pi, tan, cos, log2, e, atan, sin

r1 = 2 * tan(x + (pi / 6))
r2 = (1 / 3) + (cos(y + (x**2)) ** 2)
r3 = log2((x**2) + 2)
result = (r1 / r2) + r3

print(f"Result = {result:.2f}")