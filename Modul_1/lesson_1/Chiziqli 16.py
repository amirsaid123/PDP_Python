from math import sqrt, log, pi, tan, cos, log2, e
x, y = map(float, input().split())

result = ((2*tan((x + (pi / 6)))) / ((1 / 3) + (cos((y + x ** 2))) ** 2) + log2(x ** 2 + 2))
print(f"{result:.2f}")

