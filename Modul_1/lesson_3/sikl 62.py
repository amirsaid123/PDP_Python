from math import sin
n = int(input("Enter the number:"))
i = 1
summa = 0
while i <= n:
    summa += (((-1)**(i-1)) * ((sin(i**i)) / (2**i)))
    i += 1

print(f"{summa:.2f}")