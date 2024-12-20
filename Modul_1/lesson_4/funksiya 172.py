from math import *

def function (a, b):
    u = min(a, b)
    v = min((a*b), max(a, b))
    s = min(u + v, 3.14)
    return u, v, s




n = int(input("Enter a number:"))


print(f"{function(n):.2f}")

