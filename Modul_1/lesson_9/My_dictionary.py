name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")
address = input("Enter your address: ")


data = {
    "name": name,
    "surname": surname,
    "age": age,
    "gender": gender,
    "height": height,
    "weight": weight,
    "address": address,
}
print()
for key, value in data.items():
    print(f"{key}: {value}")
print()
print()
key_word = input("Enter your key: ")
print(data[key_word])