from math import *

def function (a, b, c):
    r1 = (2 * a) - b - sin(c)
    r2 = 5 + abs(c)
    result = r1 / r2
    return result




t, s = map(float, input("Enter:").split())

answer = function(t, (-2 * s), 1.17) + function(2.2, t, s-t)
print(f"{answer:.2f}")

