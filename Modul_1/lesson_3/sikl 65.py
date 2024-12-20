n, x = map(int, input("Enter the numbers:").split())
i = 1
summa = 0

while i <= n:
    summa += (i / (x**(2*i)))
    i += 1

print(f"{summa:.3f}")