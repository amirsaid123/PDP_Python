numbers = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

new_numbers = []
seen = []

while numbers:
    item = numbers[0]
    count = numbers.count(item)

    if count > 1 and item not in seen:
        new_numbers.append([item] * count)
        seen.append(item)

    elif count == 1 and item not in seen:
        new_numbers.append([item])
        seen.append(item)

    numbers = [x for x in numbers if x != item]

print(new_numbers)
