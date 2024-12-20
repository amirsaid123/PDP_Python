import random
import psycopg2
import faker

class PGConf:
    DBNAME = "commerce"
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



class User(PG):
    def __init__(self, fullname, email, join_date):
        self.fullname = fullname
        self.email = email
        self.join_date = join_date

class Product(PG):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order(PG):
    def __init__(self, user_id, product_id, quantity, order_date):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.order_date = order_date


f = faker.Faker()
# counter = 0
#
# def save_user_if_unique(fullname, email, join_date):
#     query = "select 1 from users where email = %s limit 1"
#     PGConf.cur.execute(query, (email,))
#     if PGConf.cur.fetchone():
#         print(f"Email {email} already exists. Skipping this record.")
#         return
#     user = User(fullname, email, join_date)
#     user.save()
#
# while counter < 100000:
#     user_data = {
#         "fullname": f.first_name() + " " + f.last_name(),
#         "email": f.email(),
#         "join_date": f.date(),
#     }
#     save_user_if_unique(**user_data)
#     counter += 1
#

# counter = 0
# while counter < 50000:
#     product_data = {
#         "name": f.word(),
#         "price": round(f.random_int(min=1, max=1000) / 100, 2),
#         "stock": f.boolean(),
#     }
#     product = Product(**product_data)
#     product.save()
#     counter += 1


# counter = 0
# while counter < 50000:
#     order_data = {
#         "user_id": f.random_int(1, 85924),
#         "product_id": f.random_int(1, 50000),
#         "quantity": f.random_int(min=1, max=10),
#         "order_date": f.date(),
#     }
#     order = Order(**order_data)
#     order.save()
#     counter += 1


