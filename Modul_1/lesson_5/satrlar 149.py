word = input('Enter a word: ')
result = word.split()
counter = 0
for i in result:
    if i.endswith("NA") or i.endswith("na") or i.endswith("nA") or i.endswith("Na"):
        print(i)
        counter += 1

print(counter)