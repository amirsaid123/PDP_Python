is_hot = False
is_cold = False
a = input("What is the weather today(hot or cold):")

if a == "hot":
    is_hot = True
elif a == "cold":
    is_cold = True



if is_hot:
    print("It`s a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It`s a cold day")
    print("Wear warm clothes")
else:
    print("It`s a lovely day")


print("Enjoy your day")
