list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9, 9]
unique = []
for i in list:
    if i not in unique:
        unique.append(i)
print(len(unique))


# string = input("Enter numbers: ")
# my_list = string.split(',')
# unique = []
# for i in my_list:
#     if i not in unique:
#         unique.append(i)
# print(len(unique))