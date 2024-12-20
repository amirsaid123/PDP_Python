class Animal:
    def __init__(self, name, gender, habitat):
        self.name = name
        self.gender = gender
        self.habitat = habitat

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.gender}, {self.habitat})"


class Bird(Animal):
    def __init__(self, name, gender,  habitat):
       super(). __init__(name, gender, habitat)


class Fish(Animal):
    def __init__(self, name, gender, habitat):
        super().__init__(name, gender, habitat)


class Mammal(Animal):
    def __init__(self, name, gender, habitat):
        super().__init__(name, gender, habitat)



b1 = Bird("Kakku", "M", "daraxt")
print(b1)