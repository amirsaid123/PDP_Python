import random
list = []
another = []
for i in range(0,10):
    list.append(random.randint(0,100))

print(list)
print("\n\n")
print("New list:")

for i in range(0,10):
    if list[i] not in another:
        another.append(list[i])

print(another)
