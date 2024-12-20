# class User:
#     pass
#
# john = User()
#
# class Shape:
#     pass
#
# circle = Shape()
#
# class Animal:
#     pass
#
# obj = Animal()



class User:
    now_year = 2024
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_birth_year(self):
        birth_year = self.now_year - self.age
        return birth_year

    def self_user_info(self):
        text = f"""
        Fullname : {self.first_name} {self.last_name}
        Age : {self.age}
        Birth Year : {self.get_birth_year()}
        """
        print(text)


ism = input("Enter your name:")
familiya = input("Enter your surname:")
yosh = int(input("Enter your age:"))

# user1 = User(ism, familiya, yosh)
# print(user1.first_name)
# print(user1.last_name)
# print(user1.age)
# print(user1.get_birth_year())

user2 = User(ism, familiya, yosh)
user2.self_user_info()

