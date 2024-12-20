from math import sin, factorial
n = int(input("Enter the number:"))
i = 1
summa = 0
while i <= n:
    summa += ((-1) ** (i-1)) * (1 / factorial(2 * i - 1))
    i += 1

print(f"{summa:.4f}")