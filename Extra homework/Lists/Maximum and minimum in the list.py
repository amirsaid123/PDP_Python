import random
list = []

for i in range(20):
    list.append(random.randint(1,100))

print(list)
maximum = max(list)
minimum = min(list)

print("Maximim = ", maximum)
print("Minimum =", minimum)
