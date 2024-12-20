"""TODO project"""
import email
from typing import Optional

users: list['User'] = []
todos = []
categories: list['Category'] = []
"""
Create
Read
Update
Delete
"""


class UserError(Exception):
    pass


# Back end
class CRUD:
    def save(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_value):
        pass

    def get(self):
        pass


class User(CRUD):
    def __init__(self,
                 _id: int = None,
                 fullname: str = None,
                 email: str = None,
                 password: str = None):
        self.id = _id
        self.fullname = fullname
        self.email = email
        self.password = password

    def delete(self):
        pass

    def update(self, field, new_value):
        pass

    def get(self):
        pass

    def about(self):
        pass

    def is_validation(self):
        pass

    def save(self):
        pass

    def login(self):
        pass

    def __repr__(self):
        return f"User(id={self.id}, fullname={self.fullname},email={self.email},password={self.password})"


class Category(CRUD):

    def __init__(self, _id=None, name=None):
        self.id = _id
        self.name = name

    def search(self, short_name):
        pass

    def about(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self, field, new_value):
        pass

    def get_list(self):
        pass

    def get(self):
        pass


class ToDo(CRUD):
    def __init__(self):
        pass


session_user: Optional['User'] = None


# Front end
class UICategory:
    session_category: Optional['Category'] = None

    def settings(self):
        menu = """
            1) delete
            2) update
            3) about
            0) <-back
            >>>"""
        match input(menu):
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "0":
                pass

    def main(self):
        try:
            menu = """
                *) Search 🔍
                1) Add
                2) List
                0) <-back
                >>>"""
            key = input(menu)
            assert key in ("*", "1", "2", "0"), "Menuyada yo'q bo'lim tanlandi"

            match key:
                case "*":
                    short_name = input("🔍>>>")

                case "1":
                    _name = input("Name:")

                case "2":
                    pass
                case "0":
                    UIAccount().panel()
        except AssertionError as message:
            print(message)
            self.main()


class UIAccount:
    def panel(self):
        menu = """
            1) Category
            2) ToDo
            0) <-back
            >>>"""
        key = input(menu)
        match key:
            case "1":
                UICategory().main()
            case "2":
                pass
            case "0":
                self.account()

    def account(self):
        print(f"Welcome to account {session_user.fullname}")
        menu = """
           1) Panel
           2) settings
           0) logout
           >>>"""
        key = input(menu)
        pass

    def edit(self):
        fields = """
                1) fullname
                2) email
                3) password
                0) <-back
                >>>"""

    def settings(self):
        menu = """
                1) Edit account
                2) About
                3) delete account
                0) <-back
                >>>"""
        key = input(menu)



class UI:

    def register(self):
        user = {
            "fullname": input("Enter your fullname:"),
            "email": input("Enter your email:"),
            "password": input("Enter your password:")
        }
        user = User(**user)
        user.is_validation()
        user.save()
        self.main()

    def login(self):
        global session_user
        login_data = {
            "email": input("Email:"),
            "password": input("Password:")
        }
        user = User(**login_data)
        session_user = user.login()
        UIAccount().account()

    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) exit
                >>>"""

            key = input(menu)
            match key:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except Exception as message:
            print(message)
            self.main()


UI().main()
