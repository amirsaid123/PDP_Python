from  math import *
a, b, c, d = map(int, input("Enter:").split())
S = 0
P = 1
m = 1
k = 1
i = 1


while m <= a:
    r1 = 3 * (m**3) + (4 * m) + 5
    r2 = (m**3) + log(m)
    result = r1 / r2
    S += result
    m += 1


while k <= b:
    P *= k / ((k**3) + 7 * k + 5)
    k += 1


SP = 0
while i <= c:
    m = 1
    sp = 1
    while m <= d:
        sp *= (log(i) + (m**i)) / m**i
        m += 1
    SP += sp
    i += 1


print(f"{S:.2f}  {P:.2f}  {SP:.2f}")


