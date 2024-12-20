import csv

# data = []
# with open("database\cars.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row)
#
# for row in data:
#     print(row)
#
#



# cars = []
# with open("database\cars.csv", "r") as f:
#     data = csv.DictReader(f)
#     for dat in data:
#         cars.append(dat)
#
#
# for car in cars:
#     print(car)





# data = [
#     ["id", "name", "position"],
#     ["1", "John Holland", "Software Engineer"],
#     ["2", "Amirsaid Samig`jonov", "CEO of Company"]
# ]
#
# with open("database/users.csv", 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile, delimiter=',')
#     csv_writer.writerows(data)
#



# data = [
#     {"id": "1", "name": "Amirsaid Samig`jonov", "position": "CEO"},
#     {"id": "2", "name": "Elon Musk", "position": "Worker"},
#     {"id": "3", "name": "Donald Trump", "position": "BodyGuard"},
# ]
#
# with open("database/users.csv", "w", newline="") as f:
#     field_names = ["id", "name", "position"]
#     writer = csv.DictWriter(f, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(data)
#
# data = []
# with open("database/users.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         data.append(row)
# for row in data:
#     print(row)
