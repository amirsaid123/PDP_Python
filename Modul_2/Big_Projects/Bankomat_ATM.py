import time
def create_color_definitions():
    colors = {
        "Reset": "\033[0m",
        "Black": "\033[30m",
        "Red": "\033[31m",
        "Green": "\033[32m",
        "Yellow": "\033[33m",
        "Blue": "\033[34m",
        "Magenta": "\033[35m",
        "Cyan": "\033[36m",
        "White": "\033[37m",
        "Bg_black": "\033[40m",
        "Bg_red": "\033[41m",
        "Bg_green": "\033[42m",
        "Bg_yellow": "\033[43m",
        "Bg_blue": "\033[44m",
        "Bg_magenta": "\033[45m",
        "Bg_cyan": "\033[46m",
        "Bg_white": "\033[47m",
    }
    return colors



user = {
    "card_number": "8600690415347786",
    "password": "1234",
    "balance": 1000,
}

colors = create_color_definitions()

class Card:
    def login(self):
        print(f"{colors['Blue']}Welcome to Bankomat PDP")
        time.sleep(1)
        limit = 3
        while limit > 0:
            temp_password = input(f"{colors['Green']}Enter your password: ")
            time.sleep(1)
            if temp_password == user["password"]:
                print(f"{colors['Green']}You successfully logged in")
                time.sleep(2)
                print("\n" * 100)
                Main_Menu().show_menu()
                return
            else:
                limit -= 1
                if limit > 0:
                    print(f"{colors['Red']}Wrong password. You have {limit} attempt(s) left. Please try again.")
                    time.sleep(1)
                else:
                    print(f"{colors['Red']}Your card is blocked!")
                    return

    def is_valid(self, password):
        return len(password) == 4

    def change_password(self, new_password):
        if self.is_valid(new_password):
            user["password"] = new_password
            print(f"{colors['Green']}Password changed successfully!")
            time.sleep(1)
            print("\n" * 100)
            self.login()
        else:
            print(f"{colors['Red']}Password is invalid. It must be 4 characters long.")
            time.sleep(2)

    def my_card(self):
        text = f"""
        Card Number = {user["card_number"]}
        Password = {user["password"]}
        Balance = {user["balance"]}$ 
        """
        return text

    def show_balance(self):
        print(f"{colors['Green']}Your current balance is {user['balance']}$")
        input(f"{colors['Green']}Press Enter to continue")
        time.sleep(2)
        print("\n" * 100)
        Main_Menu().show_menu()


class Main_Menu:

    def show_menu(self):
        print(f"{colors['Blue']}Welcome to Bankomat PDP")
        time.sleep(2)
        text = f"""
        1. Check Balance
        2. Get Cash
        3. Connect to SMS message
        4. Change Password
        5. Mobile services
        6. Credit bills
        7. Communal bills
        8. About my account
        0. Exit
        """
        print(text)
        key = input(f"{colors['Green']}Enter your choice: ")
        time.sleep(2)
        print("\n" * 100)
        match key:
            case "1":
                Card().show_balance()
            case "2":
                self.get_cash()
            case "3":
                Operations().connect_sms()
            case "4":
                old_password = input(f"{colors['Green']}Enter your old password: ")
                time.sleep(1)
                if old_password == user["password"]:
                    new_password = input(f"{colors['Green']}Enter new password: ")
                    time.sleep(1)
                    Card().change_password(new_password)
                    print("\n" * 100)
                    self.show_menu()
                else:
                    print(f"{colors['Red']}Wrong password.")
                    time.sleep(2)
                    print("\n" * 100)
                    self.show_menu()
            case "5":
                Operations().mobile()
            case "6":
                Operations().credit()
            case "7":
                Operations().communal()
            case "8":
                print(Card().my_card())
                self.show_menu()
            case "0":
                print(f"{colors['Green']}Thank you for using Bankomat PDP. Goodbye!")
                return
            case _:
                print(f"{colors['Red']}Invalid choice. Try again.")
                time.sleep(2)
                print("\n" * 100)
                self.show_menu()



    def get_cash(self):
        text = f"""{colors['Magenta']}
        1. 50$
        2. 100$
        3. 150$
        4. 200$
        5. 300$
        6. 400$
        7. Another sum
        0. Back <-
        """
        print(text)
        key = input(f"{colors['Green']}Enter your choice: ")
        time.sleep(1)
        print("\n" * 100)
        value = 0
        match key:
            case "1":
                value = 50
            case "2":
                value = 100
            case "3":
                value = 150
            case "4":
                value = 200
            case "5":
                value = 300
            case "6":
                value = 400
            case "7":
                value = int(input(f"{colors['Green']}Enter the amount of money: "))
            case "0":
                self.show_menu()
                return
            case _:
                print(f"{colors['Red']}Invalid choice. Try again.")
                time.sleep(2)
                print("\n" * 100)
                self.get_cash()
                return

        if value <= user["balance"]:
            user["balance"] -= value
            print(f"{colors['Green']}You successfully got the money.")
            time.sleep(2)
            print(f"{colors['Blue']}Your new balance is {user['balance']}$")
            print("\n" * 100)
        else:
            print(f"{colors['Red']}You don't have enough money.")
            time.sleep(2)
            print("\n" * 100)

        self.show_menu()

class Operations:


    def connect_sms(self):
        print(f"{colors['Green']}1.Turn on the SMS message")
        time.sleep(1)
        print(f"{colors['Red']}2.Turn of the SMS message")
        time.sleep(1)
        print(f"{colors['Black']}0.Back <-")
        time.sleep(1)
        key = input("Enter your choice: ")
        time.sleep(1)
        print("\n" * 100)
        match key:
            case "1":
                print(f"{colors['Green']}SMS Messages have been successfully turned on.")
                time.sleep(1)
                print("\n" * 100)
                Main_Menu().show_menu()
            case "2":
                print(f"{colors['Green']}SMS Messages have been successfully turned off.")
                time.sleep(1)
                print("\n" * 100)
                Main_Menu().show_menu()
            case "0":
                time.sleep(1)
                print("\n" * 100)
                Main_Menu().show_menu()
            case _:
                print(f"{colors['Red']}Invalid choice. Try again.")
                time.sleep(2)
                print("\n" * 100)
                Operations().connect_sms()

    def mobile(self):
        print(f"{colors['Blue']}1.Uzmobile")
        time.sleep(1)
        print(f"{colors['Yellow']}2.Beeline")
        time.sleep(1)
        print(f"{colors['Magenta']}3.Usell")
        time.sleep(1)
        print(f"{colors['Red']}4.UMS")
        time.sleep(1)
        print(f"{colors['Cyan']}5.Perfectum")
        time.sleep(1)
        print(f"{colors['Black']}0.Back <-")
        time.sleep(1)
        key = input(f"{colors['Green']}Enter your choice: ")
        time.sleep(2)
        print("\n" * 100)
        match key:
            case "1":
                number = int(input(f"{colors['Blue']}Enter the phone number: "))
                time.sleep(1)
                if int(number / 10000000) == 99:
                    value = int(input(f"{colors['Green']}Enter the amount of money: "))
                    time.sleep(1)
                    if value <= user["balance"]:
                        user["balance"] -= value
                        print(f"{colors['Green']}You successfully transferred the money.")
                        time.sleep(2)
                        print("\n" * 100)
                        Operations().mobile()
                    else:
                        print(f"{colors['Red']}You don't have enough money.")
                        print("\n" * 100)
                        Operations().mobile()
                else:
                    print(f"{colors['Red']}You phone number is incorrect! Try again.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().mobile()

            case "2":
                number = int(input(f"{colors['Blue']}Enter the phone number: "))
                time.sleep(1)
                if int(number / 10000000) == 90:
                    value = int(input(f"{colors['Green']}Enter the amount of money: "))
                    time.sleep(1)
                    if value <= user["balance"]:
                        user["balance"] -= value
                        print(f"{colors['Green']}You successfully transferred the money.")
                        time.sleep(2)
                        print("\n" * 100)
                        Operations().mobile()
                    else:
                        print(f"{colors['Red']}You don't have enough money.")
                        print("\n" * 100)
                        Operations().mobile()
                else:
                    print(f"{colors['Red']}You phone number is incorrect! Try again.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().mobile()

            case "3":
                number = int(input(f"{colors['Blue']}Enter the phone number: "))
                time.sleep(1)
                if int(number / 10000000) == 93:
                    value = int(input(f"{colors['Green']}Enter the amount of money: "))
                    time.sleep(1)
                    if value <= user["balance"]:
                        user["balance"] -= value
                        print(f"{colors['Green']}You successfully transferred the money.")
                        time.sleep(2)
                        print("\n" * 100)
                        Operations().mobile()
                    else:
                        print(f"{colors['Red']}You don't have enough money.")
                        print("\n" * 100)
                        Operations().mobile()
                else:
                    print(f"{colors['Red']}You phone number is incorrect! Try again.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().mobile()
            case "4":
                number = int(input(f"{colors['Blue']}Enter the phone number: "))
                time.sleep(1)
                if int(number / 10000000) == 97:
                    value = int(input(f"{colors['Green']}Enter the amount of money: "))
                    time.sleep(1)
                    if value <= user["balance"]:
                        user["balance"] -= value
                        print(f"{colors['Green']}You successfully transferred the money.")
                        time.sleep(2)
                        print("\n" * 100)
                        Operations().mobile()
                    else:
                        print(f"{colors['Red']}You don't have enough money.")
                        print("\n" * 100)
                        Operations().mobile()
                else:
                    print(f"{colors['Red']}You phone number is incorrect! Try again.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().mobile()
            case "1":
                number = int(input(f"{colors['Blue']}Enter the phone number: "))
                time.sleep(1)
                if int(number / 10000000) == 98:
                    value = int(input(f"{colors['Green']}Enter the amount of money: "))
                    time.sleep(1)
                    if value <= user["balance"]:
                        user["balance"] -= value
                        print(f"{colors['Green']}You successfully transferred the money.")
                        time.sleep(2)
                        print("\n" * 100)
                        Operations().mobile()
                    else:
                        print(f"{colors['Red']}You don't have enough money.")
                        print("\n" * 100)
                        Operations().mobile()
                else:
                    print(f"{colors['Red']}You phone number is incorrect! Try again.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().mobile()
            case "0":
                print("\n" * 100)
                Main_Menu().show_menu()
            case _:
                print(f"{colors['Red']}Invalid choice. Try again.")
                time.sleep(2)
                print("\n" * 100)
                Operations().mobile()

    def credit(self):
        print(f"{colors['Green']}1.Credit Card Number")
        time.sleep(1)
        print(f"{colors['Black']}0.Back <-")
        time.sleep(1)
        key = input(f"{colors['Green']}Enter your choice: ")
        time.sleep(2)
        print("\n" * 100)
        match key:
            case "1":
                number = input(f"{colors['Blue']}Enter the credit card number: ")
                time.sleep(1)
                if len(number) == 16:
                    value = int(input(f"{colors['Green']}Enter the amount of money: "))
                    time.sleep(1)
                    if value <= user["balance"]:
                        user["balance"] -= value
                        print(f"{colors['Green']}You successfully transferred the money.")
                        time.sleep(2)
                        print("\n" * 100)
                        Operations().credit()
                    else:
                        print(f"{colors['Red']}You don't have enough money.")
                        print("\n" * 100)
                        Operations().credit()
                else:
                    print(f"{colors['Red']}You credit card number is incorrect! Try again.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().credit()
            case "0":
                print("\n" * 100)
                Main_Menu().show_menu()

    def communal(self):
        print(f"{colors['Magenta']}1.Electric Energy")
        time.sleep(1)
        print(f"{colors['Red']}2.Fines")
        time.sleep(1)
        print(f"{colors['Cyan']}3.Gas")
        time.sleep(1)
        print(f"{colors['Blue']}4.Water")
        time.sleep(1)
        print(f"{colors['Black']}0.Back <-")
        key = input(f"{colors['Green']}Enter your choice: ")
        time.sleep(2)
        print("\n" * 100)
        match key:
            case "1":
                value = int(input(f"{colors['Green']}Enter the amount of money: "))
                time.sleep(1)
                if value <= user["balance"]:
                    user["balance"] -= value
                    print(f"{colors['Green']}You successfully transferred the money.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().communal()
                else:
                    print(f"{colors['Red']}You don't have enough money.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().communal()
            case "2":
                print(f"{colors['Green']}Congratulations! You do not have any fines from the government or the bank")
                time.sleep(2)
                print("\n" * 100)
                Operations().communal()
            case "3":
                value = int(input(f"{colors['Green']}Enter the amount of money: "))
                time.sleep(1)
                if value <= user["balance"]:
                    user["balance"] -= value
                    print(f"{colors['Green']}You successfully transferred the money.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().communal()
                else:
                    print(f"{colors['Red']}You don't have enough money.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().communal()
            case "4":
                value = int(input(f"{colors['Green']}Enter the amount of money: "))
                time.sleep(1)
                if value <= user["balance"]:
                    user["balance"] -= value
                    print(f"{colors['Green']}You successfully transferred the money.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().communal()
                else:
                    print(f"{colors['Red']}You don't have enough money.")
                    time.sleep(2)
                    print("\n" * 100)
                    Operations().communal()
            case "0":
                print("\n" * 100)
                Main_Menu().show_menu()
            case _:
                print(f"{colors['Red']}Invalid choice. Try again.")
                time.sleep(2)
                print("\n" * 100)
                Operations().communal()

Card().login()
