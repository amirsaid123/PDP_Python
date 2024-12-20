import random
from math import log, isfinite


numbers = [random.randint(-100, 100) for _ in range(10)]
print("Original numbers:", numbers)
print()


summa = sum(number for number in numbers if number > 0)


middle = summa / len(numbers) if len(numbers) > 0 else 0


if middle > 0:
    logarifm = log(middle)
else:
    logarifm = float('-inf')


for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = round(logarifm, 2)

print("Updated numbers:", numbers)
