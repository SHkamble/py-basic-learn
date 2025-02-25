class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age  # Private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "John":
            print("Don't set name")
        else:
            self.__name = name

    def print_details(self):
        print("Your details:", self.__name, self.__age)


# Create an instance of the class
person = Person(name="Sharan", age=24)

# Test the methods
person.set_name("sadhu")  # Proper use of set_name to change the name
name = person.get_name()  # Fetch the updated name
print(name)

# Print the details
person.print_details()
