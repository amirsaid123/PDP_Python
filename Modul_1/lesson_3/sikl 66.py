from math import sin
n, x = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += (-1) ** (i-1) * (1 / i) * sin(i * x)
    i += 1

print(f"{summa:.3f}")