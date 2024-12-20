with open("employees.txt", "r") as f:
    lines = f.readlines()


summa = 0
i = 0
for line in lines:
    summa += int(line.split(",")[2])
    i += 1


mean = summa / i
print(f"Mean salary of employees is: {mean:.0f}")
