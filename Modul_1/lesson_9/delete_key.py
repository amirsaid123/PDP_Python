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

print()
delete = input("Enter the value you want to delete:")
data.pop(delete)
print()

print()
for key, value in data.items():
    print(f"{key}: {value}")
