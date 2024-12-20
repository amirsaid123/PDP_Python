#        # 1-savol
#
# s = input("So`zlarni kiriting:")
# k = int(input("Nechta so`zni kesib olmoqchisiz:"))
# words = s.split(" ")
#
# if k <= len(words):
#     for i in range(k):
#         print(words[i], end=" ")
# else:
#     print("Siz kiritgan son indexdan tashqarida!")
#     print("Kichikroq son kiriting!")
#
#
#
#       # 2-savol
#
# n =input("Sonni kiriting:")
# summa = 0
#
#
# for i in range(len(n)-1, -1, -1):
#     print(int(n[i]), end=" ")
#     summa += int(n[i])
#
# print()
# print("Raqamlar yig`indisi =", summa)
#
#
#   # 3-savol
#
# string = input("Matnni kiriting:")
# words = string.split(" ")
# maximum = max(words, key=len)
# print("Matndagi eng uzun so`z:", maximum)
#
#
#   # 4-savol

# def count_palindrom(string:str):
#     counter = 0
#     words = string.lower().split(" ")
#     my_words = []
#     for word in words:
#         if word == word[::-1]:
#             my_words.append(word)
#             counter += 1
#     return counter, my_words
#
#
#
#
# string = input("Matnni kiriting:")
# result = count_palindrom(string)
# print("Matndagi palindrom so`zlar soni:", result)
#
#
#
# # 5-savol
# def is_Tub(n: int) -> bool:
#     result = True
#     for i in range(2, n):
#         if n % i == 0:
#             result = False
#     return result
#
# n = int(input("Son kiriting:"))
# my_tub = []
# counter = 0
# i = 2
#
# while counter != n:
#     if is_Tub(i):
#         my_tub.append(i)
#         counter += 1
#     i += 1
#
#
# my_set = set(my_tub)
#
# print(my_set)
