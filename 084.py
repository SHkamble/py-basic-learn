# Public - Variable - Don't Mention anything
# Protected-_
# Private -__
# Variable and function.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def print_details(self):
        print("Your details:", self._name, self._age)


# Instantiate the Person object outside the class definition
person = Person("sharda", 25)

# Use the get_name method to retrieve the name
name = person.get_name()
print(name)

# Call the print_details method to print the person's details
person.print_details()

# print(person.__name) # Private ?
# How to change it get and set ?
# Fetch - get
# ser the value - constructor