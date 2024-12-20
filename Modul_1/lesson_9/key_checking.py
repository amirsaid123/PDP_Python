def key_checking(key) -> bool:
    return key in data
data = {
    "name": "Amirsaid",
    "surname": "Samig`jonov",
    "age": "16",
    "gender": "Male",
    "height": "180",
    "weight": "70",
    "address": "Tashkent city",
}
print("This is our data:")
for key, value in data.items():
    print(f"{key}: {value}")

look = input("Enter a key: ")
print(key_checking(look))

