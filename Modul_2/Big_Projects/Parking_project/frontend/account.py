from typing import Optional

from tabulate import tabulate

from Modul_2.Big_Projects.Parking_project.backend.models import User
from Modul_2.Big_Projects.Parking_project.frontend.parking_ui import ParkingUI



class AccountUI:
    session_user: Optional['User'] = None
    def account(self):
        from Modul_2.Big_Projects.Parking_project.frontend.ui import session_user
        self.session_user = session_user
        print(f"Welcome {session_user.first_name} {session_user.last_name}" )

        design = [
            ["1" , "Parking"],
            ["2" , "Payment history"],
            ["0" , "logout"],
        ]
        print(tabulate(design, tablefmt="rounded_outline"))
        key = input(">>>")
        match key:
            case "1":
                ParkingUI().main()
            case "2":
                pass
            case "3":
                from Modul_2.Big_Projects.Parking_project.frontend.ui import UI
                UI().main()
