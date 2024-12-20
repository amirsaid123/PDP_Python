with open("books.txt", "r") as f:
    lines = f.readlines()


books = []

for line in lines:
    book, author = line.split(',')
    books.append([book, author])

books_sorted = sorted(books, key=lambda x: x[0].lower())

with open('books.txt', 'w') as file:
    for b in books_sorted:
        file.write(f"{b[0]}, {b[1]}" + '\n')
