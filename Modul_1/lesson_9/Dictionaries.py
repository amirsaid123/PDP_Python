# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

# x = thisdict.get("brand")
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.keys()
#
# print(x) #before the change
#
# car["color"] = "white"
#
# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.values()
#
# print(x) #before the change
#
# car["year"] = 2020
#
# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.values()
#
# print(x) #before the change
#
# car["color"] = "red"
#
# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.items()
#
# print(x) #before the change
#
# car["year"] = 2020
#
# print(x) #after the change

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # del thisdict["model"]
# # print(thisdict)
#
# for x, y in thisdict.items():
#     print(x, y)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# # # print(myfamily["child1"])
# # print(myfamily["child2"]["name"])
#
# for x, obj in myfamily.items():
#   print(x)
#
#   for y in obj:
#     print(y + ':', obj[y])


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("model", "Bronco")
#
# print(x)
