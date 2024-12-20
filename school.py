import random
from dataclasses import dataclass
import psycopg2
import faker
from datetime import timedelta

f = faker.Faker()

class PGConf:
    DBNAME = "school"
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
        [attr.pop(field) for field, value in attr.copy().items() if value is None]
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
        [conditions_attr.pop(field) for field, value in conditions_attr.copy().items() if value is None]
        args = tuple(conditions_attr.values())
        query = f"""
            select {cols} from {table_name} {self.generate_conditions(conditions_attr)}
        """
        self.cur.execute(query, args)
        data = self.to_dict()
        objects = [self.__class__(**i) for i in data]
        return objects

    def to_dict(self) -> list[dict]:
        columns = [col.name for col in self.cur.description]
        result = self.cur.fetchall()
        return [{columns[i]: row[i] for i in range(len(columns))} for row in result]

    def delete(self, *cols):
        table_name = self.__class__.__name__.lower() + "s"
        conditions_attr = self.__dict__
        [conditions_attr.pop(field) for field, value in conditions_attr.copy().items() if value is None]
        args = tuple(conditions_attr.values())
        condition_format = self.generate_conditions(conditions_attr)
        returning_cols = "returning " + " , ".join(cols) if cols else ""
        query = f"""
            delete from {table_name} {condition_format} {returning_cols}
        """
        self.cur.execute(query, args)
        self.con.commit()
        if cols:
            users = self.to_dict()
            return [self.__class__(**i) for i in users]

    def update(self, **conditions):
        table_name = self.__class__.__name__.lower() + "s"
        cols = self.__dict__
        [cols.pop(field) for field, value in cols.copy().items() if value is None]
        set_cols = " = %s , ".join(cols.keys()) + " = %s"
        condition_format = " = %s and ".join(conditions.keys()) + " = %s"
        args = tuple(list(cols.values()) + list(conditions.values()))
        query = f"""
            update {table_name} set {set_cols} where {condition_format} returning *
        """
        self.cur.execute(query, args)
        self.con.commit()
        users = self.to_dict()
        return [self.__class__(**i) for i in users]


@dataclass
class Student(PG):
    id: int = None
    first_name: str = None
    last_name: str = None
    date_of_birth: str = None
    enrolled_at: str = None
    email: str = None


@dataclass
class Teacher(PG):
    id: int = None
    first_name: str = None
    last_name: str = None
    subject: str = None


@dataclass
class Grade(PG):
    id: int = None
    student_id: int = None
    class_id: int = None
    grade: str = None


@dataclass
class Classroom(PG):
    id: int = None
    class_name: str = None
    teacher_id: str = None


# def student_fixture(count=0):
#     seen_emails = set()
#     for _ in range(count):
#         email = f.email()
#         while email in seen_emails:
#             email = f.email()
#         seen_emails.add(email)
#
#
#         user = {
#             "first_name": f.first_name(),
#             "last_name": f.last_name(),
#             "date_of_birth": f.date_of_birth(minimum_age=18, maximum_age=30).strftime('%Y-%m-%d'),
#             "enrolled_at": f.date_this_century().strftime('%Y-%m-%d'),
#             "email": email
#         }
#         Student(**user).save()
#
#
# student_fixture(1000)

#
# def teacher_fixture(count=0):
#     for _ in range(count):
#         user = {
#             "first_name": f.first_name(),
#             "last_name": f.last_name(),
#             "subject": f.word()
#         }
#         Teacher(**user).save()
#
#
# teacher_fixture(200)


def class_fixture(count=0):
    n = 1
    for _ in range(count):
        clas = {
            "class_name": random.choice(["Math", "History", "Geography", "Literature", "Computer Science"]),
            "teacher_id":n
        }
        n += 1
        Classroom(**clas).save()



class_fixture(5)


# def grade_fixture(count=0):
#     for _ in range(count):s
#         user = {
#             "student_id": f.random_int(1, 1000),
#             "class_id": f.random_int(1, 5),
#             "grade": f.random_element(["A", "B", "C", "D", "F"])
#         }
#         Grade(**user).save()
# grade_fixture(5000)
