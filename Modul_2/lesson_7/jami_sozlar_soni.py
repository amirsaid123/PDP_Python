with open("books.txt", "r") as f:
    words = f.read().split()


print(len(words))