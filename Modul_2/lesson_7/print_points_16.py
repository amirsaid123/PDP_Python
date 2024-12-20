
with open("students.txt", "r") as f:
    lines = f.readlines()


name = input("Enter a name: ")


found = False


for i, line in enumerate(lines):
    if name in line:
        print(lines[i])
        found = True
        break

if not found:
    print("Name not found in the list.")



