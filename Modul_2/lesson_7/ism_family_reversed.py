with open("books.txt", "r") as f:
    lines = f.readlines()



res = ""

for line in lines:
    book, author = line.strip().split(',')
    name, last_name = author.split()

    res += f"{book}, {last_name} {name}" + '\n'

with open('books.txt', 'w') as file:
    file.write(res)
