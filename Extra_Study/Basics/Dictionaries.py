customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# print(customer["name"])
# print(customer["age"])
# print(customer["is_verified"])
print(customer.get("birthdate", "Jan 1 1980"))