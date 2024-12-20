word = input('Enter a word: ')
result = word.split()

for i in result:
    if i.startswith("info"):
        print(i, end=" ")

