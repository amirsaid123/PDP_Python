import random

# names = ["Mosh", "John", "Amirsaid", "Said"]
# leader = random.choice(names)
# print(leader)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
