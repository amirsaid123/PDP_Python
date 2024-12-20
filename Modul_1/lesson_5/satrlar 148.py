word = input('Enter a word: ')

result = word.split()

for i in result:
    if i.startswith("A") or i.startswith("a"):
        print(i, end=" ")

