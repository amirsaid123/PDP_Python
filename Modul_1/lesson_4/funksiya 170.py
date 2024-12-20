from math import *

def function (a, b):
    r1 = a / ((b**2) + 1)
    r2 = b / ((a**2) + 1)
    r3 = (a - b) ** 3
    result = r1 + r2 - r3
    return result




s, t = map(float, input("Enter:").split())

asnwer = function(s, t) + max(function(s - t, s*t), function(s-t, s+t)) + function(1, 1)
print(f"{asnwer:.2f}")

