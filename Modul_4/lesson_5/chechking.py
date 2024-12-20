@dataclass
class Users(PG):
    id: int = None
    first_name: str = None
    last_name: str = None
    age: int = None
    passport_id: int = None
    phone_number: str = None
    email: str = None

f = faker.Faker()

for i in range(1000):
    user = {
        'first_name': f.first_name(),
        'last_name': f.last_name(),
        'age': f.random_int(min=10, max=100),
        'passport_id': f.random_int(min=1000000, max=9999999),
        'phone_number': f.phone_number(),
        'email': f.email()
    }

    Users(**user).save()