with open("employees.txt", "r") as f:
    lines = f.readlines()


found = False

name = input("Enter a name: ")

for i, line in enumerate(lines):
    if line.split(",")[0] == name:
        position = line.split(",")[1]
        salary = line.split(",")[2]
        print(f"{name},{position},{salary}")
        found = True
        break


if not found:
    print("Name not found on the list")


