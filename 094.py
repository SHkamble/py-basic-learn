# Overriding - same nae in the parent and child.
# child always override the parent functions.



class Animal:
    def speak(self):
        print("Animal speak")


class Dog(Animal):
    def speak(self):
        super().speak() # super is used for calling parent function.
        print("Dog speak")



animal = Animal()
animal.speak()

dog = Dog()
dog.speak()