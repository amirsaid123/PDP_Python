with open("employees.txt", "r") as f:
    lines = f.readlines()


found = False

name = input("Enter a name: ")

for i, line in enumerate(lines):
    if line.split(",")[0] == name:
        position = line.split(",")[1]
        salary = input("Enter a salary: ")
        lines[i] = f"{name},{position},{salary}\n"
        found = True
        break


if not found:
    print("Name not found on the list")


with open("employees.txt", "w") as f:
    f.writelines(lines)