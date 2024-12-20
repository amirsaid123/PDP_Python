from typing import Optional
from tabulate import tabulate
from Modul_2.Big_Projects.Parking_project.backend.models import map, user



class ParkingUI:
    session_user: Optional['User'] = None

    def main(self):
        from Modul_2.Big_Projects.Parking_project.frontend.account import AccountUI
        from Modul_2.Big_Projects.Parking_project.frontend.ui import session_user
        self.session_user = session_user
        design = [
            ["1", "Placing"],
            ["2", "Take out"],
            ["0", "<-back"],
        ]
        print(tabulate(design, tablefmt="rounded_outline"))
        key = input(">>>")
        match key:
            case "1":
                self.placing()
            case "2":
                self.take_out()
            case "0":
                AccountUI().account()

    def form_car(self):
        car = {
            "model" : 1
        }

    def placing(self):
        try:
            map:list = Map().make_map()
            print("0. <-back")
            pos = int(input(">>>"))
            if pos == 0:
                self.main()
            assert map[pos-1].isdigit() , "Bu joy band !"


        except AssertionError as message :
            print(message)
            print("========================================")
            self.placing()


