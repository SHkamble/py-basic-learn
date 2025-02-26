# Polymorphism
# Its a concept oops
# Object --> behave differently based on the string.
# Person --> Amit, pramod -> tallk() ,Amit can talk in hindi, pramod can talk in english
from Xlib.Xcursorfont import circle


class Shape:

    def area(self):
        print("Area of shape ")


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth


    #def area(self):
        #return self.length*self.breadth


class Circle(Shape):
     def __init__(self,radius):
         self.radius = radius

     def area(self):
            return 3.14*self.radius*self.radius


shape1 = Rectangle(3,4 )
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())

shape3 = Shape()
#shape3.area()
print(shape3.area())
print(shape2.area())
print(shape1.area())


