from dataclasses import dataclass
from datetime import timedelta

import faker
from module_4.lesson_4.ORM import PG

f = faker.Faker()


@dataclass
class User(PG):
    id: int = None
    fullname: str = None
    passport_id: str = None
    age: str = None
    phone_number: str = None
    email: str = None


@dataclass
class Book(PG):
    id: int = None
    title: str = None
    author_id: int = None
    genre_id: int = None
    published_name: str = None
    lang: str = None


@dataclass
class Rent(PG):
    id: int = None
    book_id: int = None
    user_id: int = None
    start_at: str = None
    end_at: str = None


@dataclass
class Genre(PG):
    id: int = None
    title: str = None


@dataclass
class Author(PG):
    id: int = None
    fullname: str = None
    description: str = None
    birth_date: str = None


def users_fixture(count=0):
    counter = 0
    while counter < count:
        user = {
            "fullname": f.first_name() + " " + f.last_name(),
            "passport_id": f.password(14),
            "age": f.random_int(7, 100),
            "phone_number": f.phone_number(),
            "email": f.email()
        }
        User(**user).save()
        counter += 1


users_fixture(1000)


def author_fixture(count=0):
    counter = 0
    while counter < count:
        user = {
            "fullname": f.first_name() + " " + f.last_name(),
            "description": f.text(),
            "birth_date": f.date_of_birth(minimum_age=100, maximum_age=200),
        }
        Author(**user).save()
        counter += 1


author_fixture(200)


def genre_fixture():
    for i in ["ilmiy", "baddiy", "dramma", "trello", "komedia"]:
        user = {
            "title": i
        }
        Genre(**user).save()


genre_fixture()


def book_fixture(count=0):
    counter = 0
    while counter < count:
        user = {
            "title": f.name(),
            "author_id": f.random_int(1, 200),
            "genre_id": f.random_int(1, 5),
            "published_name": f.name(),
            "lang": f.language_code(),
        }
        Book(**user).save()
        counter += 1


book_fixture(5000)


def rents_fixtures(count=0):
    counter = 0
    while counter < count:
        start_at = f.date_of_birth(minimum_age=0, maximum_age=15)
        user = {
            "book_id": f.random_int(1, 5000),
            "user_id": f.random_int(1, 1000),
            "start_at": str(start_at),
            "end_at": str(start_at + timedelta(days=7)),
        }
        Rent(**user).save()
        counter += 1


rents_fixtures(35000)
