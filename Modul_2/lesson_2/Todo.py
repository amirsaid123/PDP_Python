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

    def is_validation(self):
        for user in users:
            if user.email == self.email:
                return False, "Already exists email !"

        if len(self.password) < 4:
            return False, "Invalid password !"
        return True, "Success Valid"

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
    
        return False, "Not Found account !"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id},fullname={self.fullname},email={self.email},password={self.password})"


session_user: Optional['User'] = None


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
        is_valid, response = user.login()
        if is_valid:
            session_user = response
            self.account()
            return
        print(response)
        self.main()

    def account(self):
        print(f"Welcome to account {session_user.fullname}")

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
