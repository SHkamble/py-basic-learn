# single Inheritance -- 90% in automation used


class Animal:
    def car(self):
        print("I can drive car")



    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Bow bow")


    def i_want_drives(self):
        Animal().car()






dog = Dog()
dog.speak()
dog.i_want_drives()