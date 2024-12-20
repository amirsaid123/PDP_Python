import random

fruits = ['apple', 'pear', 'orange', 'banana']
#
# random_fruits = random.choices(fruits, weights = [10, 1, 1, 1], k=10)
# print(random_fruits)

# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# random_num = random.choices(my_numbers, k=5)
# print(random_num)


# print(random.uniform(0,1))

# my_fruits = random.sample(fruits, k=2)
# print(my_fruits)

import string


characters = string.ascii_letters + string.digits + string.punctuation


password = ''.join(random.choices(characters, k=8))
print("Random Password:", password)
