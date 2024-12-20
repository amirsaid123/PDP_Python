users: list['User'] = []
categories = ["Business", "Study", "PDP", "Sport", "School", "Household"]
todos: list['ToDo'] = []
class User:
    def __init__(self, id: int = None, fullname: str = None, email: str = None, password: str = None):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password = password

    def validate(self):
        for user in users:
            if self.email == user.email:
                return False, "Email already registered"

        if len(self.password) < 4:
            return False, "Password must be at least 4 characters"

        return True, "Successfully registered"

    def my_account(self):
        text = f"""
        Fullname: {self.fullname}
        Email: {self.email}
        Password: {len(self.password) * "*"}
        """
        return text

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
        else:
            return False, "User does not exist"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, fullname={self.fullname}, email={self.email}, password={self.password})"

class ToDo:
    statuses = ["new", "processing", "completed"]
    def __init__(self, id, title, description, category, start_time, status = "new"):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.start_time = start_time
        self.status = status

    def display(self):
        return f"""
          ToDo ID: {self.id}
          Title: {self.title}
          Description: {self.description}
          Start Time: {self.start_time}
          Category: {self.category}
          Status: {self.status}
          """



todo_1 = ToDo(1, "Reading a book", "Read 'Crime and Punishment' from literature and try to analyze it", "School", "10:30", "new")
todos.append(todo_1)
todo_2 = ToDo(2, "Work Out", "Do some sport exercises in order to be healthy and use some equipments", "sport", "20:00", "new")
todos.append(todo_2)
todo_3 = ToDo(3, "Coding", "Create an app for collecting todo lists", "PDP", "22:00", "new")
todos.append(todo_3)
todo_4 = ToDo(4, "Washing the dishes", "Wash the dishes after you have your lunch with your family. try to use thr right chemicals so that the dishes will be clean", "Household", "14:00", "new")
todos.append(todo_4)
todo_5 = ToDo(5, "Meeting with businessmen", "Organize a meeting with the company`s managers and talk about collaboration with them", "Business", "19:00", "new")
todos.append(todo_5)


session_user = None


class UI:
    def account(self):
        print(f"Welcome to your account, {session_user.fullname}")
        text = """
        1. Panel
        2. Settings
        0. Logout
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                self.panel()
            case "2":
                self.settings()
            case "0":
                Account().main_menu()

    def panel(self):
        text = """
        1.Categories
        2.ToDo
        0.Back <-
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                self.categories()
            case "2":
                self.todo()
            case "0":
                self.account()

    def categories(self):
        text = """
        1.Search
        2.List
        3.Add
        0.Back <-
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                search_value = input("Enter category name to search: ").lower()
                found_categories = [cat for cat in categories if search_value in cat.lower()]
                if found_categories:
                    print("Found categories:")
                    for i, category in enumerate(found_categories, 1):
                        print(f"{i}. {category}")
                else:
                    print("No categories found.")
                input("Press anything to go back:")
                self.categories()

            case "2":
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                key = input("Choose a category by number or press 0 to go back: ")
                if key.isdigit() and 1 <= int(key) <= len(categories):
                     self.category_menu(int(key) - 1)
                elif key == "0":
                     self.categories()

            case "3":
                new_value = input("Enter a new category name: ")
                categories.append(new_value)
                print(f"{new_value} is successfully added to categories")
                input("Press anything to go back:")
                self.categories()

            case "0":
                self.panel()

    def category_menu(self, category_index):
        category = categories[category_index]
        print(f"You selected {category}")
        text = """
        1.About
        2.View todos
        3.Update
        4.Delete
        0.Back <-
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                self.category_about(category_index)
            case "2":
                self.category_show_todos(category_index)
            case "3":
                self.category_update(category_index)
            case "4":
                self.category_delete(category_index)
            case "0":
                self.categories()


    def category_show_todos(self, category_index):
        category = categories[category_index]
        print(f"Tasks in category {category}")
        filtered_todos = [todo for todo in todos if todo.category.lower() == category.lower()]
        for todo in filtered_todos:
            print(todo.display())
        input("Press anything to go back:")
        self.category_menu(categories.index(category))

    def category_about(self, category_index):
        category_name = categories[category_index]
        category_id = category_index + 1
        number_of_tasks = len([todo for todo in todos if todo.category.lower() == category_name.lower()])
        print(f"Category ID: {category_id}, Category Name: {category_name},", "Number of Tasks: ", number_of_tasks)
        input("Press anything to go back:")
        self.category_menu(category_index)

    def category_update(self, category_index):
        new_name = input("Enter a new name for the category: ")
        categories[category_index] = new_name
        print(f"{new_name} is successfully updated!")
        input("Press anything to go back:")
        self.category_menu(category_index)

    def category_delete(self, category_index):
        category = categories[category_index]
        confirm = input(f"Do you want to delete {category}? [yes/no]:")
        if confirm == "yes":
            categories.pop(category_index)
            print(f"{category} is successfully deleted!")
        else:
            print(f"{category} is not deleted!")
        input("Press anything to go back:")
        self.categories()


    def todo(self):
        text = """
        1.View all todos
        2.Add todo
        3.Update todo
        4.Delete todo
        0.Back <-
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                self.view_todos()
            case "2":
                self.add_todo()
            case "3":
                self.update_todo()
            case "4":
                self.delete_todo()
            case "0":
                self.panel()



    def view_todos(self):
        if todos:
            for todo in todos:
                print(todo.display())
        else:
            print("No ToDos available.")
        input("Press anything to go back:")
        self.todo()

    def add_todo(self):
        id = len(todos) + 1
        title = input("Enter a title: ")
        description = input("Enter a description: ")
        start_time = input("Enter a start time: ")
        print("Choose a category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        category_index = int(input("Choose category number: ")) - 1
        category = categories[category_index]

        todo = ToDo(id, title, description, category, start_time)
        todos.append(todo)
        print(f"ToDo '{title}' added successfully!")
        input("Press anything to go back:")
        self.todo()

    def update_todo(self):
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo.title}")
        todo_index = int(input("Choose a todo to update:")) - 1
        todo = todos[todo_index]

        new_status = input("Enter a new status[new, processing, completed]: ")
        if new_status in ToDo.statuses:
            todo.status = new_status
            print(f"{new_status} is successfully updated!")
        else:
            print("Invalid status.")
        input("Press anything to go back:")
        self.todo()

    def delete_todo(self):
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo.title}")
        todo_index = int(input("Choose a ToDo to delete: ")) - 1
        todo = todos.pop(todo_index)
        print(f"ToDo '{todo.title}' deleted successfully!")
        input("Press anything to go back:")
        self.todo()




    def settings(self):
        text = """
        1. My Account
        2. Edit account
        3. Delete account
        0. Back <-
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                print(session_user.my_account())
                input("Press anything to go back: ")
                self.settings()
            case "2":
                self.edit()
            case "3":
                input_value = input("Do you agree to delete your account [yes/no]: ")
                if input_value == "yes":
                    users.remove(session_user)
                    print("Account deleted successfully.")
                    Account().main_menu()
                    return
                self.settings()
            case "0":
                self.account()

    def edit(self):
        text = """
        1. Fullname
        2. Email
        3. Password
        0. Back <-
        """
        print(text)
        key = input("Choose: ")
        match key:
            case "1":
                new_value = input("Enter new fullname: ")
                session_user.fullname = new_value
                print("Fullname updated successfully.")
                self.settings()
            case "2":
                new_email = input("Enter new email: ")
                for user in users:
                    if user.email == new_email:
                        print("Email already registered.")
                        self.settings()
                        return
                session_user.email = new_email
                print("Email updated successfully.")
                self.settings()
            case "3":
                new_password = input("Enter new password: ")
                if len(new_password) < 4:
                    print("Password must be at least 4 characters.")
                    self.settings()
                else:
                    session_user.password = new_password
                    print("Password updated successfully.")
                    self.settings()
            case "0":
                self.settings()


class Account:
    def register(self):
        user = {
            "fullname": input("Enter your full name: "),
            "email": input("Enter your email: "),
            "password": input("Enter your password: "),
        }
        user = User(**user)
        is_valid, message = user.validate()
        if is_valid:
            user.save()
        print(message)
        self.main_menu()

    def login(self):
        global session_user
        login_data = {
            "email": input("Enter your email: "),
            "password": input("Enter your password: "),
        }
        user = User(**login_data)
        is_valid, message = user.login()
        if is_valid:
            session_user = message
            UI().account()
        else:
            print(message)
            self.main_menu()

    def main_menu(self):
        text = """
        1. Register
        2. Login
        0. Exit    
        """
        print(text)
        key = input("Choose: ")
        match key:
            case '1':
                self.register()
            case '2':
                self.login()
            case '0':
                return



Account().main_menu()

