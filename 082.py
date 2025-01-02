# Encapsulation
# data members (attributes) & methods together in a class
# person --> name ,age and eat(),sleep()
# Private,Protected,Public variable



# visibility
# !! Public member
# Public members have no special naming convention in python and
# are accsesible from anywhere
# They can be accessed directly from outside the class and other modules.

# ---------------------
# !! Protected Member
# Protected members are denoted by a single underscore prefix (_).
# They can still be accessed from outside the class, but it is considered a
# best practice not to so directly.

#-------------------------
# !! Private member
# Private members are denoted by a double underscore prefix(__)
# Private members are intended to be used within the class only.



class Myclass:
    def _int_(self):
        self.public_var =10
        self.protected_var = 15

    def public_method(self):
        print("This is public method")

obj = Myclass()
obj.public_var  =34
print(obj.public_var)
obj.public_method()















