# Method Overloading.
# Python does not support method overloading in the traditional sense.
# same name of a function with different Parameter.
# MathUtils class with add method

class MathUtils:

     def add(self, a, b=0 ,c=0):
         return a + b + c

math = MathUtils()
op0 = math.add (1)
op1 = math.add (1, 2)
op2 = math.add (1, 2, 3)
print(op0)
print(op1)
print(op2)


 # math.add(1,2,3)
 ## python does not support method overloading in the traditional sense.