from math import *


x, y, a, b = map(int, input("Enter: ").split())


S = 0
a_temp = a


while a <= x:
    r1 = (a ** 2) + (2 * a)
    r2 = (a ** 3) + (a * (cos(a + 1)) ** 2)
    result = r1 / r2
    S += result
    a += 1


a = a_temp


P = 1
i = 1


while i <= y:
    P *= ((i ** 2) + 1) / ((i ** 3) ** (1 / i) + 2)
    i += 1


SP = 0

i = 1
while i <= a:
    sp = 1
    k = 1

    while k <= b:
        sp *= log((k ** i + (k ** (1 / i))) / (k ** 3 + (i ** (1 / k))))
        k += 1

    SP += sp
    i += 1

print(f"{S:.2f}  {P:.2f}  {SP:.2f}")
