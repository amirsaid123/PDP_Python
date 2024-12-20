with open("employees.txt", "r") as f:
    lines = f.readlines()


positions = [line for line in lines if line.split(",")[1]]


for i, line in enumerate(lines):
    position = line.split(",")[1]
    name = line.split(",")[0]
    salary = line.split(",")[2]
    if position in positions:
        with open(f"{position}.txt", "a") as f:
            f.writelines(f"{name},{position},{salary}\n")
    else:
        with open(f"{position}.txt", "a") as f:
            f.writelines(f"{name},{position},{salary}\n")




