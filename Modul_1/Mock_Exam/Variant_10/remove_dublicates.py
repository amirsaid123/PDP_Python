numbers = [1, 2, 3, 1, 1, 2, 2, 4, 5, 6, 7, 7, 8]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)