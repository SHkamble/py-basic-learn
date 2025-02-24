# oops concept
# construction --  method whenever object is created
from cups import modelSort
# constructor = Help to initialize the object attributes.
# Object is created a special function is called automatically_int_()
# All the attribute object you can initialize - add some initial value to them



class Car: # default constructors
    name = "sharda"  # class variable

    def __init__(self,make,model): # default con
        self.make = make # Instance variable
        self.model = model # Instance variable
        print("I will be called first")


    def start_engine(self):
        print("Starting a car", self.make,self.model)

car1 = Car("Toyota","camry")
car2 = Car("Honda","CIVIC")

car1.start_engine()
car2.start_engine()

print(id(car1))
print(id(car2))

