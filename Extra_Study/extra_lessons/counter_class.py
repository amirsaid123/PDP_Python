import random
from collections import Counter

# letters = ["A", "B", "C", "D", "E", "F"]
#
# dictionary = {}
#
#
# counter = Counter()
#
#
# for _ in range(100):
#     choice = random.choice(letters)
#     counter[choice] += 1
#
# print(counter)



letters = ["A", "B", "C", "D", "E", "F"]

occurences = random.choices(letters, k=100)

counter = Counter(occurences)
print(counter)

print(counter.most_common(1))