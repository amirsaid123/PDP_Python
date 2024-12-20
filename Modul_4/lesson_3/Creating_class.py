import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='big_data',
    user='postgres',
    password=1234,
    port=5432
)




class Database:
    def save(self):
        table_name = self.__class__.__name__.lower()

        with conn.cursor() as cursor:
            attributes = {key: type(value).__name__ for key, value in self.__dict__.items()}
            mapping = {
                "int": "INTEGER",
                "float": "FLOAT",
                "str": "VARCHAR",
                "bool": "BOOLEAN",
                "datetime": "TIMESTAMP",
                "date": "DATE"
            }

            columns = ['id serial PRIMARY KEY',]
            for value, py_type in attributes.items():
                sql_type = mapping.get(py_type, "TEXT")
                columns.append(f"{value} {sql_type}")
            create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (\n" + ",\n".join(columns) + "\n)"
            cursor.execute(create_table)
            conn.commit()

        with conn.cursor() as cursor:
            keys = list(self.__dict__.keys())
            values = list(self.__dict__.values())
            insert_table = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(['%s'] * len(values))})"

            cursor.execute(insert_table, values)
            conn.commit()

    def get(self):
        table_name = self.__class__.__name__.lower()

        with conn.cursor() as cursor:
            select_table = f"SELECT * FROM {table_name}"
            cursor.execute(select_table)
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            data = [dict(zip(columns, row)) for row in data]
        return data

    def update(self, field, current_value, new_value):
        table_name = self.__class__.__name__.lower()

        with conn.cursor() as cursor:
            update_column = f"update {table_name} set {field} = %s where {field} = %s"
            cursor.execute(update_column, (new_value, current_value))
            conn.commit()

    def delete_table(self):
        table_name = self.__class__.__name__.lower()

        with conn.cursor() as cursor:
            delete_column = f"DELETE FROM {table_name}"
            cursor.execute(delete_column)
            conn.commit()

    def delete_row(self, value):
        table_name = self.__class__.__name__.lower()

        with conn.cursor() as cursor:
            delete_column = f"DELETE FROM {table_name} WHERE id = %s"
            cursor.execute(delete_column, (value,))
            conn.commit()


class Categories(Database):
    def __init__(self, name, description, available:bool):
        self.name = name
        self.description = description
        self.available = available



category = Categories("home", "Equipments that you use at home", True)
category.save()