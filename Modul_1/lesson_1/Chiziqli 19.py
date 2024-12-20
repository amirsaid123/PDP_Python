from math import sqrt, log, pi, tan, cos, log2, e, atan
x, y = map(float, input().split())

result = log(abs(((x + y) ** 2) + sqrt(abs(y) + 2) - (x - (x * y) / (((x ** 2) / 2) - 5)))) + ((cos(x + y) ** 2) / ((x + y) ** (1/3)))
print(f"{result:.2f}")

