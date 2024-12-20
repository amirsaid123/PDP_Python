import psycopg2

class PGConf:
    DBNAME = "lesson_4"
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



from dataclasses import dataclass

import faker



@dataclass
class User(PG):
    id : int = None
    first_name : str = None
    last_name : str = None
    username : str = None
    email : str = None
    age : int = None

f = faker.Faker()
counter = 0
while counter < 1000:
    user_fake = {
        "first_name" : f.first_name(),
        "last_name" : f.last_name(),
        "username" : f.user_name(),
        "email" : f.email(),
        "age" : f.random_int(11 , 99),
    }
    user = User(username=user_fake.get('username')).objects()
    if not user:
        User(**user_fake).save()
        counter += 1
