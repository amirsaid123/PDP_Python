# users = [
#     {
#         "first_name": "Botirjon",
#         "last_name": "Qodirov",
#         "age": 17,
#         "address": "Toshkent",
#         "balance" : 100_000
#     },
#     {
#         "first_name": "Kamol",
#         "last_name": "Doniyorov",
#         "age": 17,
#         "address": "Sirdaryo",
#         "balance" : 100_000_000
#     },
# ]
# summa = 0
# for user in users:
#     FullName = user["first_name"] + " " + user["last_name"] + " " + str(user["age"])
#     print(FullName)
#     summa += user["balance"]
#
# print("Umumiy balans:", summa)

# search = input("Search:")

# for user in users:
#     FullName = user["first_name"] + " " + user["last_name"]
#     if user.get("first_name").startswith(search) or user.get("last_name").startswith(search):
#         print("Full Name:", FullName)
#         print("Age:", user["age"])
#         print("Address:", user["address"])
#         print("Balance:", user["balance"])
#     else:
#         print("Not Found")
#         break



# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# print(mytuple)