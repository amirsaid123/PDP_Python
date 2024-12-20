from math import sin, factorial

n, x = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += x ** (2 * i - 1) / (2 * i - 1)
    i += 1

print(f"{summa:.3f}")