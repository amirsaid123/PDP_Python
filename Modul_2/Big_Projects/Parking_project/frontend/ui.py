from typing import Optional

from colorama import Fore
from tabulate import tabulate
from Modul_2.Big_Projects.Parking_project.backend.models.user import User
from Modul_2.Big_Projects.Parking_project.frontend.account import AccountUI

session_user : Optional['User'] = None

class UI:
    def main(self):
        try:
            design = [
                ["1" , "Register"],
                ["2" , "Login"],
                ["3" , "exit"],
            ]
            menu = tabulate(design , tablefmt="rounded_outline")
            print(menu)
            key = input(">>>")
            match key:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except AssertionError as message:
            print(message)
            self.main()

    def register(self):
        user = {
            "first_name" : input("first_name : "),
            "last_name": input("last_name : "),
            "phone_number": input("phone_number : ")
        }
        user = User(**user)
        user.is_validation()
        user.save()
        print(Fore.GREEN + "Success Register")
        self.main()

    def login(self):
        global session_user
        auth = {
            "phone_number": input("phone_number : ")
        }
        auth = User(**auth)
        session_user = auth.is_authentication()
        AccountUI().account()





