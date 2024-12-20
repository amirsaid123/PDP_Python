numbers = {
    "apple": 15,
    "banana": 4,
    "carrot": 8,
    "dragonfruit": 62,
    "eggplant": 1,
    "fig": 9,
    "grape": 7,
    "honeydew": 3,
    "kiwi": 5,
    "lemon": 11
}

maximum = max(numbers.values())
print("Maximum =", maximum)
print("Key =", [key for key, value in numbers.items() if value == maximum])
