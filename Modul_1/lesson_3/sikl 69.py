from math import sin, factorial

n, x = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += (-1) ** 1 * ((x ** i) / factorial(i))
    i += 1

print(f"{summa:.3f}")