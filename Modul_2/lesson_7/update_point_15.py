
with open("students.txt", "r") as f:
    lines = f.readlines()


name = input("Enter a name: ")


found = False


for i, line in enumerate(lines):
    if name in line:
        point = int(input("Enter a point: "))

        lines[i] = f"{name}, {point}\n"
        found = True
        break

if not found:
    print("Name not found in the list.")


with open("students.txt", "w") as f:
    f.writelines(lines)
