import faker
f = faker.Faker()
print(f"{f.random_letter().upper()}{f.random_int(1, 10)}")