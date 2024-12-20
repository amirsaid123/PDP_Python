# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(list)):
#     list[i] = list[i] * list[i]
#
# print(list)

import random
from math import sqrt

list = []

for i in range(0,10):
    value = random.randint(0,100)
    list.append(value)

for j in range(len(list)):
    list[j] = sqrt(list[j])

print(list)
