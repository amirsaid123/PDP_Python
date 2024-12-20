class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self, width=None, height=None):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self, side=None):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self, radius=None):
        pi = 3.14
        return pi * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self, base=None, height=None):
        return self.base * self.height / 2


a = Rectangle(5, 5)
print(a.area())
b = Triangle(5, 5)
print(b.area())