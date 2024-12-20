numbers = [2, 3, 5, 6, 7, 5, 1, 9, 8, 9, 5, 10, 1, 7, 1, 3, 2, 8, 10, 2, 5, 10, 4, 1, 1, 5, 8, 3, 6, 6]
sorted_numbers = sorted(numbers)
new_list = []
i = 0
while i < len(sorted_numbers):
    number = sorted_numbers[i]
    temp = []
    while i < len(sorted_numbers) and sorted_numbers[i] == number:
        temp.append(sorted_numbers[i])
        i += 1
    new_list.append(temp)
    i += 1

print(new_list)
