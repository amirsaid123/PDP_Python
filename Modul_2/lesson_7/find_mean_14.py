with open("students.txt", "r") as f:
    lines = f.readlines()

summa = 0
i = 0
for line in lines:
     summa += int(line.split(",")[1])
     i += 1

mean = summa / i
print(mean)