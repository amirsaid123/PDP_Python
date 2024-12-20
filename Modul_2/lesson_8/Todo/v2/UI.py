from typing import Optional

from lesson_8.Todo.v2.backend import User, Category, ToDo

# ctrl + space*2

session_user: Optional['User'] = None



class UITodo:
    session_todo: Optional['ToDo'] = None
    def main(self):
        menu = """
            *) Search 🔍
            1) Add
            2) List
            0) <-back
            >>>"""
        key = input(menu)
        assert key in ("*", "1", "2", "0"), "Menuyada yo'q bo'lim tanlandi"
        match key:
            case "1":
                self.add()
            case "2":
                self.list()
            case "*":
                short_name = input("🔍>>>")
                find_todos = ToDo().search(short_name)
                for i, todo in enumerate(find_todos, 1):
                    print(f"{i}) {todo.title}")
                print("0) <-back")
                pos = input(">>>")
                if pos == "0":
                    self.main()
                    return
                self.session_todo = find_todos[int(pos) - 1]
                self.settings()

    def settings(self):
        menu = """
                    1) delete
                    2) update
                    3) about
                    0) <-back
                    >>>"""
        match input(menu):
            case "0":
                self.main()
            case "3":
                print(self.session_todo.about())
                self.settings()
            case "1":
                self.session_todo.delete()
                self.main()
            case "2":
                fields = """
                    1) title
                    2) description
                    3) start time
                    4) status
                    5) category
                    0) <-back
                >>>"""
                key = input(fields)
                if key == "0":
                    self.settings()
                    return

                match key:
                    case "1":
                        new_value = input("New title:")
                        self.session_todo = self.session_todo.update("title", new_value)

                    case "2":
                        new_value = input("New description:")
                        self.session_todo = self.session_todo.update("description", new_value)

                    case "3":
                        new_value = input("New start time:")
                        self.session_todo = self.session_todo.update("start_time", new_value)

                    case "4":
                        status = """
                            1) New
                            2) Processing
                            3) Completed
                        >>>"""
                        key = input(status)
                        _map = {
                            "1" : "new",
                            "2" : "processing",
                            "3" : "completed"
                        }
                        status = _map[key]
                        self.session_todo = self.session_todo.update("status", status)
                    case "5":
                        categories = Category().show()
                        pos = input(">>>")
                        if pos == "0":
                            self.settings()
                            return

                        choice_cat = categories[int(pos)-1]

                        self.session_todo = self.session_todo.update("category" ,choice_cat.id )
                self.settings()

    def list(self):
        todos = ToDo().show()
        pos = input(">>>")
        if pos == "0":
            self.main()
        self.session_todo = todos[int(pos)-1]
        self.settings()

    def add(self):
        categories = Category().show()

        pos = input(">>>")
        if pos == "0":
            self.main()
        todo = {
            "category" : categories[int(pos) - 1].id,
            "title" : input("Title:"),
            "description" : input("Description:"),
            "start_time" : input("Start_time:")
        }
        ToDo(**todo).save()
        self.main()

class UICategory:
    session_category : Optional['Category'] = None
    def main(self):
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
                find_categories = Category().search(short_name)
                for i, category in enumerate(find_categories,1):
                    print(f"{i}) {category.name}")
                print("0) <-back")
                pos = input(">>>")
                if pos == "0":
                    self.main()
                    return
                self.session_category = find_categories[int(pos)-1]
                self.settings()


            case "1":
                _name = input("Name:")
                Category(name=_name).save()
                self.main()

            case "2":
                categories = Category().get()
                for i, category in enumerate(categories, 1):
                    print(f"{i}) {category.name}")
                print("0) <-back")
                pos = input(">>>")
                if pos == "0":
                    self.main()
                    return
                self.session_category = categories[int(pos) - 1]
                self.settings()
            case "0":
                UIaccount().panel()

    def settings(self):
        menu = """
            1) delete
            2) update
            3) about
            0) <-back
            >>>"""
        match input(menu):
            case "1":
                self.session_category.delete()
                self.main()
            case "2":
                fields = """
                    1) name
                    0) <-back
                >>>"""
                key = input(fields)
                if key == "0":
                    self.settings()
                    return
                new_value = input("New value:")
                match key:
                    case "1":
                        self.session_category = self.session_category.update("name" , new_value)
                        self.settings()




            case "3":
                print("===============================================")
                print(self.session_category.about())
                self.settings()
                print("===============================================")
            case "0":
                self.main()

class UIaccount:

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
                UITodo().main()
            case "0":
                self.account(back=True)


    def account(self , back = False):
        if not back:
            print(f"Welcome to account {session_user.fullname}")

        menu = """
           1) Panel
           2) settings
           0) logout
           >>>"""
        key = input(menu)
        match key:
            case "1":
                self.panel()
            case "2":
                self.settings()
            case "0":
                UI().main()

    def edit(self):
        global session_user
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
                session_user = session_user.update("fullname" , new_val)
            case "2":
                User(email=new_val).is_validation()
                session_user = session_user.update("email" , new_val)
            case "3":
                User(password=new_val).is_validation()
                session_user = session_user.update("password", new_val)
        self.settings()


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
                session_user.delete()
                UI().main()
            case "0":
                self.account(back=True)

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
        session_user = user.is_authentication()
        UIaccount().account()

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
        except AssertionError as message:
            print(message)
            self.main()

UI().main()
