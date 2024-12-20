class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year


car_1 = Car("Toyota", "1996")
print(car_1.__model)
