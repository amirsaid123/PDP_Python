list_of_lists = [[1,2,3], [4,5,6], [7,8,9], [1, 2, 3], [13, 14, 15], [7, 8, 9]]
unique = []

for list in list_of_lists:
    if list not in unique:
        unique.append(list)

print(unique)
