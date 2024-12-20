from math import sqrt, log, pi, tan, cos, log2, e, atan
x, y = map(float, input().split())

result = (((1 / (x + (2 / (x**2)) + (3 / (x**3)))) + (e ** ((x ** 2) + 3*x))) / (atan(x + y) + (abs(5 + x) ** 2))) - (cos(y ** 2 + ((x ** 2 )/ 2)) ** 2)
print(f"{result:.2f}")

