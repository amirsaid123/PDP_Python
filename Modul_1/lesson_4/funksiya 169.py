from math import *

def function (a, b):
    u = min(a, b)
    v = min((a*b), max(a, b))
    s = min(u + v, 3.14)
    return u, v, s




a, b = map(float, input("Enter:").split())

result = function(a, b)
print(f"{result[0]:.2f}, {result[1]:.2f}, {result[2]:.2f}")

