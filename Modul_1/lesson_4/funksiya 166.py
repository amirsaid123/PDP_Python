from math import *

def function (a, b):
    r1 = (a**2) + (b**2)
    r2 = (a**2) + (2 * a * b) + (3 * (b**2)) + 4
    result = r1 / r2
    return result




t, s = map(float, input("Enter:").split())

answer = function(1.2, s) + function(t, s) + function(2 * s - 1, s*t)
print(f"{answer:.2f}")

