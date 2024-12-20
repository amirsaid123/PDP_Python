import json



# with open("database\centers.json", "r") as f:
#     data = f.read()
#

# id = int(input("Enter your id:"))
#
#
# for dat in data:
#     if dat["id"] == id:
#         for key, value in dat.items():
#             print(f"{key}: {value}")


# name = "Chippewa"
#
# for data in data:
#     if data["name"] == name:
#         for key, value in data.items():
#             print(f"{key}: {value}")
#         print()


# counts = {}
# for dat in data:
#     name = dat["name"]
#     if name in counts:
#         counts[name] += 1
#     else:
#         counts[name] = 1
#
#
# for key, value in counts.items():
#     print(f"{key}: {value}")
#


# =================================================================================================================





with open("database/products.json", "r") as f:
    products = json.load(f)


new_product = {
    "id": products[-1].get("id") + 1 if products else 1,
    "name": "Xiaomi 12 Ultra",
    "price": "2000$"
}

products.append(new_product)

with open("database/products.json", "w") as f:
    json.dump(products, f, indent=4)

