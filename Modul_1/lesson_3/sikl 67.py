from math import sqrt
n, x = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += (x**i) / (sqrt(i))
    i += 1

print(f"{summa:.3f}")