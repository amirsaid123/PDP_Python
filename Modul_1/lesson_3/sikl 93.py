from math import *
x, y, a, b = map(int, input("Enter:").split())

S = 0
k = 1

while k <= x:
    r1 = (k**2) + sin(k) + 5
    r2 = ((k**7) + 1) ** (1/5)
    S += (r1 / r2)
    k += 1

P = 1
n = 1

while n <= y:
    v1 = n + sqrt(n)
    v2 = (n - ((n+1) ** (1/5)))
    P *= (v1 / v2)
    n += 1

SP = 0
k = 1
while k <= a:
    i = 1
    sp = 1
    while i <= b:
        j1 = ((i**2) + (k**2 ** (2/i)))
        j2 = (sin(i) + cos(k)) * (i**k)
        sp *= (j1 / j2)
        i += 1
    k += 1
    SP += sp

print(f"{S:.2f}  {P:.2f}  {SP:.2f}")