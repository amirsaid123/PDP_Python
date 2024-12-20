import random
from dataclasses import dataclass
from typing import Optional
from os.path import join
from colorama import Fore
from Modul_2.Big_Projects.Parking_project.backend.models.utils import File, BASE_DIR, DB_PATH


@dataclass
class User(File):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    card_id: Optional[int] = None


    def send_code(self):
        code = str(random.randrange(10**5, 10**6))
        with open(join(DB_PATH, "code.txt"), "w") as f:
            f.write(code)
        return code

    def is_validation(self):
        users:list['User'] = self.get()
        for user in users:
            assert user.phone_number != self.phone_number, Fore.RED + "Already exists"

        code = self.send_code()
        input_code = input("Enter a code:")
        assert input_code == code, Fore.RED + "Invalid code"

    def is_authentication(self):
        users:list['User'] = self.get()
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.send_code()
                input_code = input(Fore.GREEN + "Enter a code:")
                assert input_code == code, Fore.RED + "Invalid code"
                return user
