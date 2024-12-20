import psycopg2
import faker
import random
import psycopg2
from datetime import timedelta



class PGConf:
    DBNAME = "cinema"
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



class Movie(PG):
    def __init__(self, title, genre, release_date):
        self.title = title
        self.genre = genre
        self.release_date = release_date




f = faker.Faker()



# while counter < 500000:
#     movie_data = {
#         "title": f.sentence(),
#         "genre": random.choice(["Science Fiction", "Comedy", "Fantasy", "Documentary", "Drama", "Thriller"]),
#         "release_date": f.date(),
#     }
#     movie = Movie(**movie_data)
#     movie.save()
#     counter += 1


class Actor(PG):
    def __init__(self, fullname, age, country, birth_date):
        self.fullname = fullname
        self.age = age
        self.country = country
        self.birth_date = birth_date



# while counter < 50000:
#     actor_data = {
#         "fullname": f.first_name() + " " + f.last_name(),
#         "age": f.random_int(16, 90),
#         "country": f.country(),
#         "birth_date": f.date(),
#     }
#     actor = Actor(**actor_data)
#     actor.save()
#     counter += 1

counter = 0
class Bridge(PG):
    def __init__(self, movie_id, actor_id):
        self.movie_id = movie_id
        self.actor_id = actor_id



while counter < 62022:
    bridge_data = {
        "movie_id": random.randint(1, 500000),
        "actor_id": random.randint(1, 50000),
    }
    bridge = Bridge(**bridge_data)
    bridge.save()
    counter += 1