from datetime import timedelta

import faker
import random, string
import psycopg2


class PGConf:
    DBNAME = "library"
    USER = "postgres"
    PASSWORD = "1234"
    HOST = "localhost"
    PORT = 5432
    con = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
    cur = con.cursor()


class PG(PGConf):

    def generate_conditions(self, conditions_attr):
        conditions_format = " where " + " = %s and ".join(conditions_attr.keys()) + " = %s" if conditions_attr else ""
        return conditions_format

    def save(self):
        table_name = self.__class__.__name__.lower() + "s"
        attr = self.__dict__
        [attr.pop(field) for field, value in attr.copy().items() if value == None]
        cols = " , ".join(attr.keys())
        format = " , ".join(["%s"] * len(attr.keys()))
        args = tuple(attr.values())
        query = f"""
            insert into {table_name} ({cols}) values ({format})
        """
        self.cur.execute(query, args)
        self.con.commit()

    def objects(self, *columns):
        table_name = self.__class__.__name__.lower() + "s"
        cols = " , ".join(columns) if columns else "*"
        conditions_attr = self.__dict__
        [conditions_attr.pop(field) for field, value in conditions_attr.copy().items() if value == None]
        args = tuple(conditions_attr.values())
        query = f"""
            select {cols} from {table_name} {self.generate_conditions(conditions_attr)}
        """

        self.cur.execute(query, args)
        data: list[dict] = self.to_dict()
        objects = []
        for i in data:
            objects.append(self.__class__(**i))
        return objects

    def to_dict(self) -> list[dict]:
        columns = list(self.cur.description)
        result = self.cur.fetchall()
        results = []
        for row in result:
            row_dict = {}
            for i, col in enumerate(columns):
                row_dict[col.name] = row[i]
            results.append(row_dict)
        return results

    def delete(self, *cols):
        table_name = self.__class__.__name__.lower() + "s"
        conditions_attr = self.__dict__
        [conditions_attr.pop(field) for field, value in conditions_attr.copy().items() if value == None]
        args = tuple(conditions_attr.values())
        condition_format = self.generate_conditions(conditions_attr)
        returning_cols = "returning " + " , ".join(cols) if cols else ""
        query = f"""
            delete from {table_name} {condition_format} {returning_cols}"""
        self.cur.execute(query, args)
        self.con.commit()
        if cols:
            users = self.to_dict()
            if users:
                objects = []
                for i in users:
                    objects.append(self.__class__(**i))
                return objects

    def update(self, **conditions):
        table_name = self.__class__.__name__.lower() + "s"
        cols = self.__dict__
        [cols.pop(field) for field, value in cols.copy().items() if value == None]
        set_cols = " = %s , ".join(cols.keys()) + " = %s"
        condition_format = " = %s and ".join(conditions.keys()) + " = %s  "
        args = tuple(list(cols.values()) + list(conditions.values()))
        query = f"""
            update {table_name} set {set_cols} where {condition_format} returning *
        """
        self.cur.execute(query, args)
        self.con.commit()
        users = self.to_dict()
        if users:
            objects = []
            for i in users:
                objects.append(self.__class__(**i))
            return objects




#
# class User(PG):
#     def __init__(self, fullname, age, phone_number, passport_id, email):
#         self.fullname = fullname
#         self.age = age
#         self.phone_number = phone_number
#         self.passport_id = passport_id
#         self.email = email
#
#
# import random
#
#
# def generate_uzbek_phone_number():
#     country_code = "+998"
#     operator_code = random.choice(range(90, 100))
#     number = "".join(random.choices("0123456789", k=7))
#     return f"{country_code}{operator_code}{number}"
#
#
#
#
#
# def generate_passport_id():
#     prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
#     numbers = ''.join(random.choices(string.digits, k=7))
#     return f"{prefix}{numbers}"
#
#
#
#
# f = faker.Faker()
#
# counter = 0
#
# while counter < 1000:
#     user_data = {
#         "fullname": f.first_name() + "  " + f.last_name(),
#         "age": f.random_int(16, 100),
#         "phone_number": generate_uzbek_phone_number(),
#         "passport_id": generate_passport_id(),
#         "email": f.email(),
#     }
#     user = User(**user_data)
#     user.save()
#     counter += 1


# class Book(PG):
#     def __init__(self, title, author_id, genre_id, publisher_name, language):
#         self.title = title
#         self.author_id = author_id
#         self.genre_id = genre_id
#         self.publisher_name = publisher_name
#         self.language = language
#
#
#
#
#
# f = faker.Faker()
#
# counter = 0
#
# while counter < 5000:
#     book_data = {
#         "title": f.sentence(),
#         "author_id": f.random_int(1, 200),
#         "genre_id": f.random_int(1, 5),
#         "publisher_name": random.choice(["Asaxiy", "Abu-saxiy", "Yoshlar agentligi", "Kitobxon.uz", "Yosh kitobxon"]),
#         "language": random.choice(["Uzbek", "English", "Russian", "Turkish", "Arabic"]),
#     }
#     book = Book(**book_data)
#     book.save()
#     counter += 1



class Rent(PG):
    def __init__(self, book_id, user_id, start_at, end_at):
        self.book_id = book_id
        self.user_id = user_id
        self.start_at = start_at
        self.end_at = end_at


f = faker.Faker()

counter = 0

while counter < 35000:
    rent_data = {
        "book_id": f.random_int(1, 5000),
        "user_id": f.random_int(1, 1000),
        "start_at": f.date(),
        "end_at": f.date(),
    }

    rent = Rent(**rent_data)
    rent.save()
    counter += 1


# class Author(PG):
#     def __init__(self, fullname, description, birth_date, death_date ):
#         self.fullname = fullname
#         self.description = description
#         self.birth_date = birth_date
#         self.death_date = death_date
#
#
#
# f = faker.Faker()
#
# counter = 0
#
# while counter < 200:
#     author_data = {
#         "fullname": f.first_name() + "  " + f.last_name(),
#         "description": f.text(300),
#         "birth_date": f.date(),
#         "death_date": f.date()
#     }
#
#     author = Author(**author_data)
#     author.save()
#     counter += 1
