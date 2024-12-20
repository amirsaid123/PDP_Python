import random
numbers = []
n = int(input("Listning uzunligi:"))
for i in range(n):
    numbers.append(random.randint(-100,100))

print("Bizning list:", numbers)

# maximum = max(numbers)
# print("Birinchi eng katta son =", maximum)
#
# numbers = [num for num in numbers if num != maximum]
#
# second_maximum = max(numbers)
# print("Ikkinchi eng katta son =", second_maximum)

sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)
print("Second max =", sorted_numbers[1])
