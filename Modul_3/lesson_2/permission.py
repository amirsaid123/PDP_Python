# User database
users = [
    {"id": 1, "username": "botir", "password": "1111", "role": "ADMIN"},
    {"id": 2, "username": "baxa", "password": "2222", "role": "USER"},
    {"id": 3, "username": "jamol", "password": "0000", "role": "USER"},
    {"id": 4, "username": "zafar", "password": "4444", "role": "USER"},
    {"id": 5, "username": "aziz", "password": "5555", "role": "USER"},
    {"id": 6, "username": "umid", "password": "6666", "role": "USER"},
    {"id": 7, "username": "shoxrux", "password": "7777", "role": "USER"},
    {"id": 8, "username": "dilshod", "password": "8888", "role": "USER"},
    {"id": 9, "username": "hasan", "password": "9999", "role": "USER"},
    {"id": 10, "username": "nodir", "password": "1010", "role": "ADMIN"}
]


def authenticate(username, password):
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                return user
            else:
                print("Wrong password")
                return None
    print("Not found username")
    return None


def permission(required_role):
    def inner(func):
        def wrapper(*args, **kwargs):
            username = kwargs.get("username")
            password = kwargs.get("password")

            user = authenticate(username, password)
            if not user:
                return "Authentication failed"

            if user["role"] != required_role:
                return "Permission denied"

            return func(*args, **kwargs)
        return wrapper
    return inner


@permission("ADMIN")
def summa(*args, username, password):
    return sum(args)


print(summa(1,2,3, username="nodir", password="1010"))