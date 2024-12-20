import psycopg2, faker, random


class PGConf:
    DBNAME = "university"
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




class Department(PG):
    def __init__(self, name):
        self.name = name

class Professor(PG):
    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id

class Student(PG):
    def __init__(self, name, grouup):
        self.name = name
        self.grouup = grouup

class Enrollment(PG):
    def __init__(self, student_id, professor_id, course_name, grade):
        self.student_id = student_id
        self.professor_id = professor_id
        self.course_name = course_name
        self.grade = grade


f = faker.Faker()

counter = 1
while counter <= 10:
    department_data = {
        "name": f.company()
    }
    department = Department(**department_data)
    department.save()
    counter += 1

counter = 1
while counter <= 50:
    professor_data = {
        "name": f.name(),
        "department_id": f.random_int(1, 10),
    }
    professor = Professor(**professor_data)
    professor.save()
    counter += 1


counter = 1
while counter <= 500:
    student_data = {
        "name": f.name(),
        "grouup": f.random_int(1, 25),
    }
    student = Student(**student_data)
    student.save()
    counter += 1


counter = 1
while counter <= 1000:
    enrollment_data = {
        "student_id": f.random_int(1, 500),
        "professor_id": f.random_int(1, 50),
        "course_name": random.choice(["Computer Science", "Math", "Literature", "History", "Politics", "Economics", "Social Science", "Psychology", "Philosophy", "Engineering"]),
        "grade": random.choice(["A", "B", "C", "D", "E", "F"]),
    }
    enrollment = Enrollment(**enrollment_data)
    enrollment.save()
    counter += 1