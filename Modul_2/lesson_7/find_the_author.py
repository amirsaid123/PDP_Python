
with open("books.txt", "r") as f:
    lines = f.readlines()

found = False
name = input("Enter a name of the book: ")


for line in lines:
    if name in line:
        found = True
        print(f"Author: {line.split(',')[1]}")

if found:
    print(f"Books by {name} have been added to name_books.txt.")
else:
    print(f"No books found by {name}.")


