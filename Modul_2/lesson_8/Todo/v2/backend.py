from typing import Optional

DB_PATH = "D:\PDP Python\Modul_2\lesson_8\Todo\v2\database"

from dataclasses import dataclass


class File:
    def save(self) -> None:
        file_name = self.__class__.__name__.lower() + "s.txt"

        datas: list = self.get()
        self.id = int(datas[-1].id) + 1 if datas else 1
        datas.append(self)
        result = []
        for obj in datas:
            tmp = "|".join(map(str, obj.__dict__.values())).strip()
            result.append(tmp)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write("\n".join(result))

    def get(self) -> list:
        file_name = self.__class__.__name__.lower() + "s.txt"
        with open(f"{DB_PATH}/{file_name}") as f:
            data = f.readlines()
        for i, item in enumerate(data):
            data[i] = self.__class__(*item.split("|"))
        return data

    def update(self, field, new_value):
        file_name = self.__class__.__name__.lower() + "s.txt"
        datas = self.get()
        for i in datas:
            if i.id == str(self.id):
                setattr(i, field, new_value)
                session_user = i
        result = []
        for obj in datas:
            tmp = ",".join(map(str, obj.__dict__.values())).strip()
            result.append(tmp)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write("\n".join(result))
        return session_user


    def delete(self) -> None:
        file_name = self.__class__.__name__.lower() + "s.txt"
        datas = self.get()
        for i in datas:
            if i.id == str(self.id):
                datas.remove(i)
        result = []
        for obj in datas:
            tmp = ",".join(map(str, obj.__dict__.values())).strip()
            result.append(tmp)
        with open(f"{DB_PATH}/{file_name}", "w") as f:
            f.write("\n".join(result))


@dataclass
class User(File):
    id :Optional[str] = None
    fullname:Optional[str] = None
    email:Optional[str] = None
    password:Optional[str] = None

    def is_validation(self):
        users: list[User] = self.get()
        for user in users:
            assert self.email and user.email != self.email, "Already exists"
        assert self.password and  len(self.password) >= 4 , "Invalid password"
        assert self.email and  self.email.endswith("@gmail.com") , "Invalid email"

    def is_authentication(self)->'User':
        users:list['User'] = self.get()
        for user in users:
            if user.email == self.email:
                assert user.password == self.password , "Wrong password"
                return user
        raise AssertionError("Not found account")

    def about(self):
        text = f"""
            id : {self.id}
            fullname : {self.fullname}
            email : {self.email}
            password : {self.password}
        """
        return text


@dataclass
class Category(File):
    id : str = None
    name : str = None

    def show(self):
        categories = self.get()
        for index , category in enumerate(categories,1):
            print(f"{index}) {category.name}")
        print("0) <-back")
        return categories


    def search(self , search_value)->list['Category']:
        categories: list['Category'] = self.get()
        result = []
        for category in categories:
            if search_value.lower() in category.name.lower():
                result.append(category)
        return result

    def about(self):
        text = f"""
            id : {self.id}
            name : {self.name}
        """
        return text

@dataclass
class ToDo(File):
    id : str = None
    title : str = None
    description : str = None
    start_time : str = None
    category : str = None
    status : str = "new"

    def search(self , search_value):
        todos = self.get()
        result = []
        for todo in todos:
            if search_value.lower() in todo.title.lower():
                result.append(todo)
        return result
    def about(self):
        text = f"""
            id: {self.id}
            title: {self.title}
            description: {self.description}
            start_time: {self.start_time}
            status: {self.status}
            category: {self.category}
        """
        return text
    def show(self):
        todos = self.get()
        for pos , todo in enumerate(todos,1):
            print(f"{pos}) {todo.title}")
        print("0) <-back")
        return todos










