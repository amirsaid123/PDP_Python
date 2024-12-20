from math import *

def function (a, b, c):
    r1 = max(a, a + b) + max(a, b + c)
    r2 = 1 + max(a + (b*c), 1.15)
    result = r1 / r2
    return result




a, b, c = map(float, input("Enter:").split())

answer = function(a, b, c)
print(f"{answer:.2f}")

