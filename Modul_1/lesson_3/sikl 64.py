n, x = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += (-1) ** (i-1) * (1 / (x**(2*i)))
    i += 1

print(f"{summa:.3f}")