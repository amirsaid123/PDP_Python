
with open("books.txt", "r") as f:
    lines = f.readlines()

found = False
name = input("Enter a name: ")


for line in lines:
    if name in line:
        found = True

        with open("name_books.txt", "a") as f:
            f.write(line)


if found:
    print(f"Books by {name} have been added to name_books.txt.")
else:
    print(f"No books found by {name}.")


with open("name_books.txt", "r") as f:
    print(f.read())
