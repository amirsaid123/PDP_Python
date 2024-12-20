from math import sin, factorial

n, k = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += (1 - k) * (((-1) ** i) * ((k ** i)) / factorial(i))
    i += 1

print(f"{summa:.3f}")