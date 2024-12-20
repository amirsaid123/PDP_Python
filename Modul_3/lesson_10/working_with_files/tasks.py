import json, csv


# with open("database/centers.json", "r") as f:
#     centers = json.load(f)
#
#
# with open("database/centers.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=centers[0].keys())
#     writer.writeheader()
#     for center in centers:
#         writer.writerow(center)
#



data = []

with open("database/cars.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)


with open("database/cars.json", "w") as file:
    json.dump(data, file, indent=4)

