from math import sin
n = int(input("Enter the number:"))
i = 0
summa = 0
while i <= n:
    summa += (sin(i) / (2**i))
    i += 1

print(f"{summa:.2f}")
