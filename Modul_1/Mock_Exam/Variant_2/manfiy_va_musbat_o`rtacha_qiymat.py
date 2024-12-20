import random
numbers = []

n = int(input("Enter a number: "))
for i in range(n):
    numbers.append(random.randint(-100,100))

print("List:", numbers)
print()

sum_positive = 0
number_positive = 0
sum_negative = 0
number_negative = 0
for number in numbers:
    if number > 0:
        sum_positive += number
        number_positive += 1
    else:
        sum_negative += number
        number_negative += 1


print("Musbat sonlar o`rtacha qiymati =", round(sum_positive / number_positive, 2))
print("Manfiy sonlar o`rtacha qiymati =", round(sum_negative / number_negative, 2))