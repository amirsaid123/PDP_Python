"""TODO project"""
from typing import Optional

"""
1) database architecture
2) database
3) backend
4) UI
"""

"""
User:
    id
    fullname
    email
    password

Category:
    id
    name

ToDo:
    id
    title
    description
    start_time
    category : Category
    status [new,processing , completed]

"""

# Auth:
#     register
#     login
users: list['User'] = []
todos = []
categories = []


class User:
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 email: str = None,
                 password: str = None):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password = password

    def about(self):
        text = f"""
            Fullname : {self.fullname}
            Email : {self.email}
            password : {len(self.password) * "*"}
"""
        return text

    def is_validation(self):
        for user in users:
            if self.email and user.email == self.email:
                return False, "Already exists! "
        if self.password and len(self.password) < 4:
            return False, "Invalid password"
        return True, "Success"

    def save(self):
        self.id = users[-1].id + 1 if users else 1
        users.append(self)

    def login(self):
        for user in users:
            if user.email == self.email:
                if user.password == self.password:
                    return True, user
                else:
                    return False, "Wrong password"
        return False, "Not found"

    def __repr__(self):
        pass


session_user: Optional['User'] = None


class UIAccount:
    def account(self):
        print(f"Welcome to account {session_user.fullname}")

        menu = """
           1) Panel
           2) settings
           0) logout
           >>>"""
        key = input(menu)
        match key:
            case "1":
                pass
            case "2":
                self.settings()
            case "0":
                UI().main()

    def edit(self):
        fields = """
            1) fullname
            2) email
            3) password
            0) <-back
            >>>"""
        field = input(fields)
        if field == "0":
            self.settings()
            return

        new_val = input("New value")
        match field:
            case "1":
                session_user.fullname = new_val
            case "2":
                is_valid , message = User(email = new_val).is_validation()
                if is_valid:
                    session_user.email = new_val
                print(message)
                self.settings()
            case "3":
                is_valid, message = User(password=new_val).is_validation()
                if is_valid:
                    session_user.password = new_val
                print(message)
                self.settings()

            case "0":
                UI().main()


    def settings(self):
        menu = """
                1) Edit account
                2) About
                3) delete account
                0) <-back
                >>>"""
        key = input(menu)
        match key:
            case "1":
                self.edit()
            case "2":
                print(session_user.about())
                self.settings()
            case "3":
                users.remove(session_user)
                UI().main()
            case "0":
                self.account()


class UI:

    def register(self):
        user = {
            "fullname": input("Enter your fullname:"),
            "email": input("Enter your email:"),
            "password": input("Enter your password:")
        }
        user = User(**user)
        is_valid, message = user.is_validation()
        if is_valid:
            user.save()
        print(message)
        self.main()

    def login(self):
        global session_user
        login_data = {
            "email": input("Email:"),
            "password": input("Password:")
        }
        user = User(**login_data)
        is_login, response = user.login()
        if is_login:
            session_user = response
            UIAccount().account()
            return
        print(response)
        self.main()

    def main(self):
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


UI().main()
# Deadline : 19:50
