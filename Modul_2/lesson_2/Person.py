class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


class Customer(Person):
    def __init__(self, name, surname, age, gender, customer_id, balance):
        super().__init__(name, surname, age, gender)
        self.customer_id = customer_id
        self.balance = balance



class Employee(Person):
    def __init__(self, name, surname, age, gender, salary, workplace):
        super(). __init__(name, surname, age, gender)
        self.salary = salary
        self.workplace = workplace



class Manager(Employee):
    def __init__(self, name, surname, age, gender, salary, employees, workplace):
        super().__init__(name, surname, age, gender, salary, workplace)
        self.employees = employees
        self.workplace = workplace



class Developer(Employee):
    def __init__(self, name, surname, age, gender, salary, programming_language, workplace):
        super().__init__(name, surname, age, gender, salary, workplace)
        self.programming_language = programming_language


