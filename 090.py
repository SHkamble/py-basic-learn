# Hierarchial  Inheritance:

class Vehicle:
    def  info (self):
        return "This is a Vehicle"


class Car(Vehicle):
    def info (self):
        return "This is a Car"


class Bicycle(Vehicle):
    def info (self):
        return "This is a Bicycle"

car = Car()
bicycle = Bicycle()
print(car.info())
print(bicycle.info())

