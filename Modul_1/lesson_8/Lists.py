# l = ["Hello", "World", 1, 2, 3, [4, 5, 6], [12, 16, 19], ["a", "b", "c"], "amir", 1.5]

# for item in l:
#     if isinstance(item, list):
#         for num in item:
#             if str(num).isdigit() and num % 2 == 0:
#                 print(num)

# for  item in l:
#     if isinstance(item, list):
#         for num in item:
#             if isinstance(num, int) and num % 2 == 0:
#                 print(num)

# [print(num) for item in l if isinstance(item, list) for num in item if isinstance(num, int) and num % 2 == 0]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print([number for number in numbers if number % 2 == 0])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(["Juft" if number % 2 == 0 else "Toq" for number in numbers])


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(sum(numbers))
# summa = 0
# [(summa := summa + i) for i in numbers]
# print(summa)

numbers = [1, 2, 3, 2, 5, 6, 2, 8, 9, 9, 10, 1]
maximum = 0
num = 0
# for i in range(len(numbers)):
#     if numbers.count(numbers[i]) > maximum:
#         maximum = numbers.count(numbers[i])
#         num = numbers[i]
# print(num, maximum)
numbers.sort()
